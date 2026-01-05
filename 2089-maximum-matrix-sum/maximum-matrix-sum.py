class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        min_abs_val = float('inf')
        num_of_neg = 0
        total_sum = 0
        for i in range (m):
            for j in range (n):
                total_sum += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    num_of_neg += 1
                min_abs_val = min(min_abs_val, abs(matrix[i][j]))
        if num_of_neg % 2 == 0:
            return total_sum
        return total_sum - 2 * min_abs_val
        

        