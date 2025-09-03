from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # sort by x asc, and for equal x sort by y desc
        points.sort(key=lambda p: (p[0], -p[1]))

        n = len(points)
        count = 0
        for A in range(n - 1):
            bottom_right_y = -10**18  # safe very small value
            for B in range(A + 1, n):
                if points[B][1] <= points[A][1] and points[B][1] > bottom_right_y:
                    count += 1
                    bottom_right_y = points[B][1]
        return count