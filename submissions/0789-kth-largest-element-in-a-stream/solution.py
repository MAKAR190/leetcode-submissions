# Edge cases
# - 

# Suggested approach
# nums = heap = [] - should we transform it in the add function each time and work with the heap as a copy of nums heapified or just initialize them as a heap at default constructor
# implementing add:
# add a new score "val" to the heap, but if the heap is more than "k" length we pop the smallest one  
# return the largest kth val which should be our last element
# 

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.nums = nums
        
        while len(self.nums) > k:
            heapq.heappop(self.nums)
           
    def add(self, val: int) -> int:
            if len(self.nums) < self.k:
                heapq.heappush(self.nums, val)
            else:
                heapq.heappush(self.nums, val)
                heapq.heappop(self.nums)
        
            return self.nums[0]
        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
