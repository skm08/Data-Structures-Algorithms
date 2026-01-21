class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        sol = []
        for x in nums:
            if x % 2 == 0:
                sol.append(-1)
            else:
                t = 0
                while x & (1 << t):
                    t += 1
                sol.append(x ^ (1 << (t - 1)))
        return sol