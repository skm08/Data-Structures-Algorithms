class Solution:
    def minimumDeletions(self, s: str) -> int:
        return reduce(lambda dp,c: 
            (dp[0], dp[1]+1) if c=='b' else (dp[0]+1 if dp[0]<dp[1] else dp[1], dp[1]), 
            s, (0,0)
        )[0]
        