# Edge cases and questions

# Approach
# heap = []

# Iterate through points and calculate the distance between the point and the origin and then push that point straight into the heap (min heap)

# Do it until we reach it for K times (so K closest points)
# Return the heap
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:        
        heap = []
        
        for x, y in points:
            d = -(x**2 + y**2) 
            if len(heap) < k:
                heapq.heappush(heap, (d, [x, y]))
            else:
                if d > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (d, [x, y]))

                
        
        return [point for _, point in heap]
            
            
        
