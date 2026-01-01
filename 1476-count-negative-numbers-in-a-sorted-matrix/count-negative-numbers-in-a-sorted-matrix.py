class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        output: int = 0
        m: int = len(grid[0])
        hor: int = m - 1
        for i in range(len(grid)):
            while hor >= 0 and grid[i][hor] < 0: hor -= 1
            output += m - hor - 1
        return output