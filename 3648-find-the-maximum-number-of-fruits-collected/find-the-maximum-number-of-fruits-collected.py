from typing import List
from functools import lru_cache

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        # child 1: main diagonal is fixed
        diag = sum(fruits[i][i] for i in range(n))

        # -------------------------------
        # helpers for the other two kids
        # -------------------------------
        child2_moves = [(1, -1), (1, 0), (1, 1)]      # starts (0, n-1)
        child3_moves = [(-1, 1), (0, 1), (1, 1)]      # starts (n-1, 0)

        # “allowed” predicates keep a kid in its own triangle
        def above_diag(x, y):   # x < y  (plus the goal cell)
            return x < y or (x, y) == (n-1, n-1)

        def below_diag(x, y):   # x > y  (plus the goal cell)
            return x > y or (x, y) == (n-1, n-1)

        @lru_cache(None)
        def dfs2(x: int, y: int) -> int:          # kid #2
            if (x, y) == (n-1, n-1):
                return fruits[x][y]
            best = float('-inf')
            for dx, dy in child2_moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and above_diag(nx, ny):
                    best = max(best, dfs2(nx, ny))
            return fruits[x][y] + best

        @lru_cache(None)
        def dfs3(x: int, y: int) -> int:          # kid #3
            if (x, y) == (n-1, n-1):
                return fruits[x][y]
            best = float('-inf')
            for dx, dy in child3_moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and below_diag(nx, ny):
                    best = max(best, dfs3(nx, ny))
            return fruits[x][y] + best

        top_right  = dfs2(0, n-1)        # start of kid #2
        bottom_left = dfs3(n-1, 0)       # start of kid #3

        # bottom-right cell counted three times – keep only one copy
        return diag + top_right + bottom_left - 2 * fruits[-1][-1]