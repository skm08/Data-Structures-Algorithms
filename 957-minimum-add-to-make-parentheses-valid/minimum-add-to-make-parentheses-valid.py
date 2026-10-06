class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = add = 0 # s = "())"
        for ch in s:
            if ch == "(":
                open += 1
            elif open:
                open -= 1
            else:
                add += 1
        return add + open