class Solution:
    def numOfSubarrays(self, arr):
        MOD = 1000000007
        odd_count, even_count, prefix_sum, result = 0, 1, 0, 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                result = (result + odd_count) % MOD
                even_count += 1
            else:
                result = (result + even_count) % MOD
                odd_count += 1

        return result