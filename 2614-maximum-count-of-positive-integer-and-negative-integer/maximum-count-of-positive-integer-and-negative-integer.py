from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums):
        n = len(nums)
        lb = bisect_left(nums, 0)
        ub = bisect_right(nums, 0)
        
        return max(lb, n - ub)