class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        neg = -10**18
        m,n = len(nums1),len(nums2)
        dp = [[neg]*(n+1) for _ in range(m+1)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                prod = nums1[i] * nums2[j]
                take = prod + max(0,dp[i+1][j+1])
                dp[i][j] = max(take,dp[i+1][j],dp[i][j+1])
        return dp[0][0]