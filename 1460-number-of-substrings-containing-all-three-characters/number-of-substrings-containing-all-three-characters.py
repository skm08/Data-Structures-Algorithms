class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        subarrays = 0
        freq = [0, 0, 0]  # Frequency array for 'a', 'b', 'c'

        left = 0
        for right in range(n):  # Expand window to the right
            freq[ord(s[right]) - ord('a')] += 1  # Increment frequency of current character
            while all(f > 0 for f in freq):  # Valid window found
                subarrays += n - right  # All subarrays starting at left and ending at right or beyond are valid
                freq[ord(s[left]) - ord('a')] -= 1  # Slide window from left
                left += 1
        return subarrays