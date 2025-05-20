import heapq

class Solution:
    # Difference array approach
    def isZeroArray(self, nums, queries):
        n = len(nums)
        diff = [0] * (n + 1)
        
        for start, end in queries:
            diff[start] += 1
            if end + 1 < n:
                diff[end + 1] -= 1
        
        current = 0
        for i in range(n):
            current += diff[i]
            if current < nums[i]:
                return False
        return True

    # Heap approach
    def isZeroArrayHeap(self, nums, queries):
        queries.sort()
        min_heap = []
        query_pos = 0
        
        for i in range(len(nums)):
            # Add all queries starting with i
            while query_pos < len(queries) and queries[query_pos][0] == i:
                heapq.heappush(min_heap, queries[query_pos][1])
                query_pos += 1
            
            if len(min_heap) < nums[i]:
                return False
            
            # Remove queries that end at i
            while min_heap and min_heap[0] == i:
                heapq.heappop(min_heap)
        
        return True