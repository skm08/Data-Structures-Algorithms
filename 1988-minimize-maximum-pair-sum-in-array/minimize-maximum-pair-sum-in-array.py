class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        largest = -1

        left, right = 0, len(nums) - 1
        while left < right:
            candidate = nums[left] + nums[right]
            if candidate > largest:
                largest = candidate
            left += 1
            right -= 1
        return largest