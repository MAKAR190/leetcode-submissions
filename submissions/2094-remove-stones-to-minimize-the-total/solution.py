# Defining the problem
# We need to return the minimum possible sum of stones in piles array while decreasing elements only K times

# Possible approach
# Create a heap (max heap) where we could decrease max elements, because the best way to decrease sum to minimal sum is by decreasing its max elements

# Edge cases
# -

# Pseudo-algorithm
# 1. Initialize a max heap
# 2. Pop the max element and halve it using floor(piles[i] / 2)
# 3. Repeat 2 step k times
# 4. Return stones' sum

import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        
        for _ in range(k):
            #max_element = heapq.heappop(piles)
            #max_element = floor(max_element / 2)
            #heapq.heappush(piles, max_element)
        
            heapq.heappush(piles, floor(heapq.heappop(piles) / 2))

        return -sum(piles)
            
            
