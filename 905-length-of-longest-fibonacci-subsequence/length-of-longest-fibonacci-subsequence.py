class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        values = set(arr)
        longest = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]
                fib_len = 2
                while a + b in values:
                    a, b = b, a + b
                    fib_len += 1
                if fib_len > 2:
                    longest = max(longest, fib_len)
        return longest