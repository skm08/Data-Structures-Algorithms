class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ans=0
        for i in range(0,len(grid)):
            for j in range (1,len(grid[i])):
                grid[i][j]+=grid[i][j-1]
        for i in range(1,len(grid)):
            for j in range(0,len(grid[i])):
                grid[i][j]+=grid[i-1][j]
        for ar in grid:
            for e in ar:
                if e<=k:
                    ans+=1
        return ans 