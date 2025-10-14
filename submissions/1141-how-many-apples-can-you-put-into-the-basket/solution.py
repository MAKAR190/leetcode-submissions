import heapq
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        heapq.heapify(weight)
        apples = 0
        total = 0

        while weight and weight[0] + total <= 5000:
            total += heapq.heappop(weight)
            apples += 1
        
        return apples
