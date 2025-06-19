class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        subsequences = 1
        min_val = nums[0]

        for i in range(1, n):
            if nums[i] - min_val > k:
                min_val = nums[i]
                subsequences += 1
        return subsequences