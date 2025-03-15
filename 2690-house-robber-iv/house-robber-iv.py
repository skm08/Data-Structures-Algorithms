from typing import List

class Solution:
    def canAssign(self, max_val: int, nums: List[int], k: int) -> bool:
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] <= max_val:
                count += 1
                i += 1  # Skip the next house
            i += 1
        return count >= k

    def minCapability(self, nums: List[int], k: int) -> int:
        low = min(nums)
        high = max(nums)
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
            if self.canAssign(mid, nums, k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans