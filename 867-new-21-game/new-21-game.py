class Solution:
    """
    check my soln
    """
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k==0 or n >= k+maxPts:
            return 1.0
        
        #dp[x] = the probability reaching score x
        dp = [0.0]*(n+1)
        dp[0] = 1.0
        windowSum = 1.0
        result = 0.0

        for x in range(1, n+1):
            dp[x] = windowSum/maxPts

            if x < k:
                windowSum += dp[x]
            else:
                result += dp[x]
            
            #shrink window
            if x - maxPts >= 0:
                windowSum -= dp[x - maxPts]
        
        return result
                