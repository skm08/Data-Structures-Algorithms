class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        blacks = 0
        recolors = float('inf')

        for i in range(n):
            if blocks[i] == 'B':
                blacks += 1
            
            if i >= k-1:
                recolors = min((k - blacks), recolors)
                if blocks[i-k+1] == 'B':
                    blacks -= 1
        return recolors