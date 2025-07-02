class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9+7
        if not word:
            return 0
        
        # Gather count per group for
        # consecutive characters
        groups, x = [], 1
        for i in range(1,len(word)):
            if word[i] == word[i-1]:
                x += 1
            else:
                groups.append(x)
                x = 1
        groups.append(x)

        # Get the total and check if
        # the number of groups already
        # satisfy the condition
        total = 1
        for i in groups:
            total = (total * i) % MOD
        if k <= len(groups):
            return total
        
        # DP to get invalid values and return
        # (valid - invalid)
        dp = [0] * k
        dp[0] = 1

        for i in groups:
            tmp = [0] * k
            x = 0
            for s in range(k):
                if s > 0:
                    x = (x + dp[s-1]) % MOD
                if s > i:
                    x = (x-dp[s-i-1]) % MOD
                tmp[s] = x
            dp = tmp
        
        invalid = sum(dp[len(groups):k]) % MOD
        return (total-invalid) % MOD