class Solution:
    def minimumLength(self, s: str) -> int:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        length = 0
        for count in freq:
            if count % 2 == 1:
                length += 1
            else:
                length += min(2, count)
        
        return length