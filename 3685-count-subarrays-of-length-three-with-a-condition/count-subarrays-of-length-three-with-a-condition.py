class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(n-2):
            first = nums[i]
            middle = nums[i+1]
            third = nums[i+2]

            if (first + third) * 2 == middle:
                count += 1
        return count