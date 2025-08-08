from math import ceil
dp: list[list[float]] = [[-1] * 201 for _ in range(201)]
class Solution:
    def dfs(self, a: int, b: int) -> float:
        if a <= 0 and b <= 0: return 0.5
        elif a <= 0 and b > 0: return 1
        elif a > 0 and b <= 0: return 0
        if dp[a][b] != -1: return dp[a][b]
        dp[a][b] = 0.25 * (self.dfs(a - 4, b) + self.dfs(a - 3, b - 1) + self.dfs(a - 2, b - 2) + self.dfs(a - 1, b - 3))
        return dp[a][b]
    def soupServings(self, n: int) -> float:
        if n > 4450: return 1
        bound: int = ceil(n / 25)
        return self.dfs(bound, bound)
        