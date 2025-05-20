class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)

        diff = [0] * (n+1)
        for l, r in queries:
            diff[l] += 1
            diff[r+1] -= 1

        rsum = 0
        for i in range(n):
            rsum += diff[i]
            if nums[i] > rsum:
                return False
        return True