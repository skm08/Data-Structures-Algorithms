class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if nums[i] < nums[j]:
                    res = max(res,(nums[j]-nums[i]))
        return res