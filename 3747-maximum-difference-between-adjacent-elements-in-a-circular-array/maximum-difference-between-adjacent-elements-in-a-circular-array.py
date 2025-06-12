class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_dist = 0
        
        # Check adjacent elements
        for i in range(1, len(nums)):
            max_dist = max(max_dist, abs(nums[i] - nums[i-1]))
        
        # Check wrap-around
        max_dist = max(max_dist, abs(nums[0] - nums[-1]))
        
        return max_dist