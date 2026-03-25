class Solution:
    def canPartitionGrid(self, grid):
        n = len(grid)
        m = len(grid[0])

        total = 0

        # Calculate total sum
        for i in range(n):
            for j in range(m):
                total += grid[i][j]

        # If total is odd, cannot split equally
        if total % 2 != 0:
            return False

        req = total // 2

        # Check horizontal cuts
        rowsum = 0
        for i in range(n - 1):
            for j in range(m):
                rowsum += grid[i][j]
            if rowsum == req:
                return True

        # Check vertical cuts
        colsum = 0
        for j in range(m - 1):
            for i in range(n):
                colsum += grid[i][j]
            if colsum == req:
                return True

        return False