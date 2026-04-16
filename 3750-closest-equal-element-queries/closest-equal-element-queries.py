from typing import List
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        
        # Group indices by value
        pos = defaultdict(list)
        for i, val in enumerate(nums):
            pos[val].append(i)
        
        # For each value, compute minimum distance to another occurrence
        for val, indices in pos.items():
            m = len(indices)
            if m > 1:
                for i in range(m):
                    idx = indices[i]
                    left = indices[i - 1]
                    right = indices[(i + 1) % m]
                    # Circular distance to left
                    d1 = abs(idx - left)
                    d_left = min(d1, n - d1)
                    # Circular distance to right
                    d2 = abs(idx - right)
                    d_right = min(d2, n - d2)
                    ans[idx] = min(d_left, d_right)
        
        # Answer queries
        return [ans[q] for q in queries]