class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def backtrack():
            res = 0
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    res += 1
                    res += backtrack()
                    count[c] += 1
            return res
        return backtrack()

# class Solution:
#     def buildString(self, freq: list[int]) -> int:
#         ways = 0
#         for i in range(26):
#             if freq[i] > 0:
#                 freq[i] -= 1
#                 ways += 1 + self.buildString(freq)
#                 freq[i] += 1
#         return ways

#     def numTilePossibilities(self, tiles: str) -> int:
#         freq = [0] * 26
#         for c in tiles:
#             freq[ord(c) - ord('A')] += 1
#         return self.buildString(freq)