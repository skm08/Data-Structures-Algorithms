class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        MOD = 10**9 + 7

        def get_all_consecutive_sums(fences, limit):
            # add boundary fences
            fences = [1] + sorted(fences) + [limit]
            
            # compute gaps
            gaps = []
            for i in range(1, len(fences)):
                gaps.append(fences[i] - fences[i - 1])
            
            # prefix sum for fast subarray sum
            prefix = [0]
            for g in gaps:
                prefix.append(prefix[-1] + g)

            sums = set()
            k = len(gaps)
            for i in range(k):
                for j in range(i + 1, k + 1):
                    sums.add(prefix[j] - prefix[i])
            return sums

        # get all possible heights and widths
        horizontal = get_all_consecutive_sums(hFences, m)
        vertical = get_all_consecutive_sums(vFences, n)

        # find maximum common side
        max_side = 0
        for side in horizontal:
            if side in vertical:
                max_side = max(max_side, side)

        if max_side == 0:
            return -1

        return (max_side * max_side) % MOD