class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = current_sum
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]: 
                current_sum += nums[i]  # Extend ascending subarray
            else:
                current_sum = nums[i]  # Start a new subarray
                
            max_sum = max(max_sum, current_sum)  # Update max sum
        
        return max_sum