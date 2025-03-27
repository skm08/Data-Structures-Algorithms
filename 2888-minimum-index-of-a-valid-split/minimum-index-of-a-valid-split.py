class Solution:
    def mooresVotingAlgo(self,nums):
        majority_element = nums[0]
        freq = 1
        for i in range(1,len(nums)):
            if nums[i] != majority_element:
                freq -= 1
            else:
                freq += 1
            if freq == 0:
                majority_element = nums[i]
                freq = 1
        return majority_element

    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        majority_element = self.mooresVotingAlgo(nums)
        max_freq = nums.count(majority_element)

        prefix_count = 0
        for i in range(n-1):
            if nums[i] == majority_element:
                prefix_count += 1
                max_freq -= 1
            if (prefix_count > (i+1)//2) and (max_freq > (n-i-1) // 2):
                return i
        return -1