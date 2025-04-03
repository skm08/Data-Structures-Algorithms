class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_diff = 0
        max_left = 0
        max_val = 0

        for num in nums:
            max_val = max(max_val,max_diff * num)
            max_diff = max(max_diff, max_left-num)
            max_left = max(max_left, num)
        return max_val