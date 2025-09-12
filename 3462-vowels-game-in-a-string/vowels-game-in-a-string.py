class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for ch in s:
            if ch in ('a','e','i','o','u'):
                return True
        return False