class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)

        # Initialize blocks
        block_size = int(n**0.5)+1 # Add one to handle non perfect squares
        blocks = [0] * (block_size)

        # Fill blocks with max value per block in one pass
        curr_max = 0
        for idx, size in enumerate(baskets):
            # If we are starting a new block, the new max is first the basket size in block
            if idx%block_size == 0:
                curr_max = size
            curr_max = max(size, curr_max)
            blocks[idx // block_size] = curr_max
        
        idx = 0
        ans = n # Set ans to n as every time we pick a fruit, we decrement
        for fruit in fruits:
            found = False # Flag to stop once we find fruit
            for b in range(len(blocks)):
                # If the max basket size in this block is below fruit, skip it
                if blocks[b] < fruit: 
                    continue
                
                # There exists a basket size in this block that can fit the fruits, loop over the block
                for j in range(b*block_size, min(n, (b+1)*block_size)):
                    if baskets[j] >= fruit:
                        found = True
                        baskets[j] = -1 # Mark as -1 as a size cannot be negative 
                        ans -= 1
                        # Update the current block with the new max value now that we used the best basket
                        # This operation is O(sqrt(n))
                        blocks[b] = max(
                            [baskets[i] for i in range(b*block_size, min(n, (b+1)*block_size))]
                        )
                        break
                if found: 
                    break

        return ans