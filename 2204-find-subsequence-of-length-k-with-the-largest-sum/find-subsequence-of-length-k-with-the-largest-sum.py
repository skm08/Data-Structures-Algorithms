class Solution:
    def maxSubsequence(self, nums, k):
        # Step 1: Pair number with index
        pairs = [(num, i) for i, num in enumerate(nums)]
        
        # Step 2: Sort by number descending
        pairs.sort(key=lambda x: -x[0])
        
        # Step 3: Take top k
        top_k = pairs[:k]
        
        # Step 4: Sort by original index
        top_k.sort(key=lambda x: x[1])
        
        # Step 5: Return only the numbers
        return [num for num, _ in top_k]