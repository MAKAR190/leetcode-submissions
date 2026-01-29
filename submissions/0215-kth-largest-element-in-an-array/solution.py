import heapq

# [3,2,1,5,6,4]
# [5, 6]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            
            while len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]
