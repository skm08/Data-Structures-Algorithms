class Solution:
    def divideArray(self, nums):
        remaining = set()
        for ele in nums:
            if ele in remaining:
                remaining.remove(ele)
            else:
                remaining.add(ele)
        return len(remaining) == 0