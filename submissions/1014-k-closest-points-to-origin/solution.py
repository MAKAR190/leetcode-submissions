class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        
        for x, y in points:
            distance = sqrt(x**2 + y**2)
            heapq.heappush(min_heap, (-distance, [x, y]))
            
            while len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [heap_element[1] for heap_element in min_heap]
                
