class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_sub = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                candidate = num[i:i+3]
                if candidate > max_sub:
                    max_sub = candidate
        return max_sub