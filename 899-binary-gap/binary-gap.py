class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        if s.count("1") <= 1:
            return 0
        res = 0
        i = 0
        for j in range(1, len(s)):
            if s[i] == "1" and s[j] == "1" and "1" not in s[i+1:j]:
                temp = j - i
                res = max(temp, res)
                i = j
        return res