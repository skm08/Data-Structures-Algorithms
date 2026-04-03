from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        bots = sorted(zip(robots, distance))
        ws = sorted(walls)
        n = len(bots)

        def cw(lo, hi):
            if lo > hi: return 0
            return bisect_right(ws, hi) - bisect_left(ws, lo)

        L, R = [], []
        for i in range(n):
            pos, dist = bots[i]
            lo = max(pos - dist, bots[i-1][0] + 1) if i > 0 else pos - dist
            hi = min(pos + dist, bots[i+1][0] - 1) if i < n-1 else pos + dist
            L.append((lo, pos))     
            R.append((pos, hi))     

        dp_l = cw(*L[0])
        dp_r = cw(*R[0])

        for i in range(1, n):
            wl = cw(*L[i])
            wr = cw(*R[i])

            ov_lo = max(R[i-1][0], L[i][0])
            ov_hi = min(R[i-1][1], L[i][1])
            overlap = cw(ov_lo, ov_hi)

            new_dp_l = max(
                dp_l + wl,           
                dp_r + wl - overlap  
            )
            new_dp_r = max(
                dp_l + wr,           
                dp_r + wr            
            )

            dp_l, dp_r = new_dp_l, new_dp_r

        return max(dp_l, dp_r)