class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        stk = []

        for i in range(len(pattern) + 1):
            stk.append(str(i + 1))
            if i == len(pattern) or pattern[i] == "I":
                while stk:
                    res.append(stk.pop())
        ans = "".join(res)
        return ans