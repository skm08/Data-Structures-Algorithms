class Solution:
    def minOperations(self, grid, x):
        array = []
        remainder = grid[0][0] % x

        # Step-1: Insert array elements
        for row in grid:
            for num in row:
                if num % x != remainder:
                    return -1  # Impossible to make Uni-Value Grid
                array.append(num)

        # Step-2: Sort 1D array
        array.sort()
        n = len(array)
        median = n // 2

        # Step-3: Count steps required
        steps = 0
        for num in array:
            steps += abs(num - array[median]) // x

        return steps