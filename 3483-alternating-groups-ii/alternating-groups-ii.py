from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        count = 0
        l = 0
        limit = n + k - 1

        while l < n:
            # Find largest valid window
            r = l + 1
            while r < limit and colors[(r - 1) % n] != colors[r % n]:
                r += 1

            # Count Valid Windows
            if r - l >= k:
                count += (r - l) - k + 1
            l = r

        return count