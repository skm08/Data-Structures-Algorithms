class Solution:
    def countSetBits(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
    
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits = self.countSetBits(num2)
        result = 0
        for i in range(31, -1, -1):
            if bits > 0 and (num1 & (1 << i)):
                result |= (1 << i)
                bits -= 1
        for i in range(32):
            if bits > 0 and not (result & (1 << i)):
                result |= (1 << i)
                bits -= 1
        return result