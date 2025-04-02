class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        left = nums[0]
        for j in range(1,n):
            if left < nums[j]:
                left = nums[j]
            for k in range(j+1,n):
                res = max(res, ((left - nums[j]) * nums[k]))
        return res