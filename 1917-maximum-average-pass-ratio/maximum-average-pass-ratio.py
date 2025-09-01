import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classData: List[List[int]], extra: int) -> float:
        
        # Function to compute improvement if one student is added
        def improvement(passed: int, total: int) -> float:
            return (passed + 1) / (total + 1) - passed / total

        # Priority queue (max heap based on improvement)
        heap = [(-improvement(p, t), p, t) for p, t in classData]
        heapq.heapify(heap)

        # Assign each extra student greedily
        for _ in range(extra):
            gain, passed, total = heapq.heappop(heap)
            passed += 1
            total += 1
            heapq.heappush(heap, (-improvement(passed, total), passed, total))

        # Calculate overall average pass ratio
        result = sum(p / t for _, p, t in heap) / len(classData)
        return result