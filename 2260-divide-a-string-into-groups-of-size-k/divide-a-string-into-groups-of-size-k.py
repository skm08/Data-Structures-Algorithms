class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        n = len(s)
        i = 0
        while i < n:
            char = s[i:i+k]
            if len(char) < k:
                num = k - len(char)
                char += fill * num
            result.append(char)
            i += k
        return result