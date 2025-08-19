class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        size = 0
        total = 0
        for n in nums:
            if n == 0:
                size += 1
            else:
                if size != 0:
                    total += (size * (size + 1)) // 2
                    size = 0
        if size != 0:
            total += (size * (size + 1)) // 2
        return total