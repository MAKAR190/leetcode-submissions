# Defining the problem
# nums = [2, 4, 9, 7] n * log(n) using sorting
# Find the largest k-th element (prefering not using sorting)


# Prefered approach
# heap = [] - min heap
# iterate through nums, push to the heap each one, but if heap exceeds k length, we pop from the heap
# 

# TC and SC
# SC(k) and TC(n * log(k))

# Debugging

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: # k = 2
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
            
            if len(heap) > k:
                heapq.heappop(heap)
            
        return heapq.heappop(heap)
        
