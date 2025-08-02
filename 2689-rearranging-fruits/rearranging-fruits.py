from typing import List
import sys

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        n = len(basket1)
        min_val = sys.maxsize
        balance = {}
        
        # Build balance map and track global minimum
        for x, y in zip(basket1, basket2):
            balance[x] = balance.get(x, 0) + 1
            balance[y] = balance.get(y, 0) - 1
            min_val = min(min_val, x, y)
        
        # Collect values that need to be transferred
        transfers = []
        for val, bal in sorted(balance.items()):
            if bal & 1:
                return -1  # cannot balance
            transfers.extend([val] * (abs(bal) // 2))
        
        # Pair the smallest surpluses
        transfers.sort()
        cost = 0
        m = len(transfers)
        for i in range(m // 2):
            cost += min(transfers[i], 2 * min_val)
        
        return cost