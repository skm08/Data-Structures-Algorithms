class Solution:
    def flipWindow(self, nums, pos):
        nums[pos] ^= 1
        nums[pos+1] ^= 1
        nums[pos+2] ^= 1

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0

        for i in range(n-2):
            if nums[i] == 1:
                continue
            self.flipWindow(nums, i)
            operations += 1

        if nums[n-2] == 0 or nums[n-1] == 0:
            return -1
        
        return operations