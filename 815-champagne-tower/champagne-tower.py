class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        # Initialize memo table with -1.0 (representing uncalculated states)
        # The tower has at most 100 rows
        t = [[-1.0 for _ in range(101)] for _ in range(101)]
        
        def solve(i, j):
            # Out of bounds: No liquid flows from non-existent glasses
            if i < 0 or j < 0 or j > i:
                return 0.0
            
            # Base Case: The top glass receives all poured champagne
            if i == 0 and j == 0:
                return poured
            
            # Return memoized result if available
            if t[i][j] != -1.0:
                return t[i][j]
            
            # Calculate overflow from the two glasses above
            # (Amount in parent - 1) / 2
            up_left = (solve(i - 1, j - 1) - 1) / 2.0
            up_right = (solve(i - 1, j) - 1) / 2.0
            
            # Only positive overflow is distributed
            up_left = max(0.0, up_left)
            up_right = max(0.0, up_right)
            
            # Store and return the total liquid passing through this glass
            t[i][j] = up_left + up_right
            return t[i][j]
        
        # Result cannot exceed the glass capacity of 1.0
        return min(1.0, solve(query_row, query_glass))