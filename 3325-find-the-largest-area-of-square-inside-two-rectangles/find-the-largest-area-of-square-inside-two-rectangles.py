class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        side = 0

        for i in range(len(bottomLeft)):
            for j in range(i + 1, len(topRight)):
                ai, bi = bottomLeft[i]
                aj, bj = bottomLeft[j]
                ci, di = topRight[i]
                cj, dj = topRight[j]

                left = max(ai, aj)
                right = min(ci, cj)
                bottom = max(bi, bj)
                top = min(di, dj)

                if left >= right or bottom >= top:
                    continue

                width = right - left
                height = top - bottom

                side = max(side, min(width, height))

        return side ** 2
