from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Handle the edge case for numRows = 0
        if numRows == 0:
            return []

        # Start with the first row
        triangle = [[1]]

        # Loop to generate the remaining rows
        for i in range(numRows - 1):
            # Get the previous row
            prev_row = triangle[-1]
            
            # Start the new row with a 1
            new_row = [1]
            
            # Calculate the middle elements by summing adjacent pairs
            for j in range(len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j+1])
            
            # End the new row with a 1
            new_row.append(1)
            
            # Add the completed new row to our triangle
            triangle.append(new_row)
            
        return triangle