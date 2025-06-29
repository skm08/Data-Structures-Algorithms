class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        power_of_two = [1] * n
        for i in range(1, n):
            power_of_two[i] = (power_of_two[i - 1] * 2) % MOD
        
        nums.sort()
        subsequences = 0
        left, right = 0, n - 1
        
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                subsequences = (subsequences + power_of_two[right - left]) % MOD
                left += 1
        return subsequences