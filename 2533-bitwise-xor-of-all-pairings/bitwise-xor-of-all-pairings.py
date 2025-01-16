class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        m = len(nums2)
        if m % 2 == 1:
            for ele in nums1:
                ans ^= ele
        n = len(nums1)
        if n % 2 == 1:
            for ele in nums2:
                ans ^= ele
        return ans