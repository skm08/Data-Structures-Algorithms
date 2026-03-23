class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        results = []
        inBound = lambda i, j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
        @cache
        def backtrack(i, j, res):
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                results.append(res * grid[i][j])
                return
            for di, dj in [[0,1], [1, 0]]:
                if inBound(i + di, j + dj):
                    backtrack(i + di, j + dj, res * grid[i][j])
        backtrack(0, 0, 1)
        return max(results) % MOD if max(results) > -1 else -1