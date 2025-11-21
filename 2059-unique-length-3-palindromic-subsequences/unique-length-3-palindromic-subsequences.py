class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # left = [float('inf')] * 26
        # right = [-1] * 26
        # res = 0
        # for i, char in enumerate(s):
        #     left[ord(char) - ord('a')] = min(left[ord(char) - ord('a')], i)
        #     right[ord(char) - ord('a')] = i

        # for i in range(26):
        #     if left[i] < right[i]:
        #         res += len(set(s[left[i] + 1 : right[i]]))
        # return res

        if len(s) <= 2:
            return 0
        chars = set(s)
        res = 0
        for c in chars:
            left = s.find(c)
            right = s.rfind(c)
            if left != right:
                res += len(set(s[left + 1 : right]))
        return res