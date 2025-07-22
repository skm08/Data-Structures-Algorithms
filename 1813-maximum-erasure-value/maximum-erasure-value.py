class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        n = len(nums)
        val_idx = set()

        max_sum = float('-inf')
        win_sum = 0
        while right < n:
            if nums[right] in val_idx:
                val_idx.remove(nums[left])
                win_sum -= nums[left]
                left += 1
            else:
                win_sum += nums[right]
                val_idx.add(nums[right])
                right += 1
                max_sum = max(max_sum, win_sum)
        return max_sum