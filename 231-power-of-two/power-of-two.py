class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is positive and has only one bit set in its binary representation
        return n > 0 and (n & (n - 1)) == 0
