class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        for i in range(len(n)):
            ans = ans if ans > (ord(n[i]) - ord('0')) else (ord(n[i]) - ord('0'))
        return ans