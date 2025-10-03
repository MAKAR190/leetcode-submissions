import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        total_cost = 0
        
        while len(sticks) > 1:
            n = len(sticks)
            temp_cost = 0
            
            for _ in range(min(2, n)):
                temp_cost += heapq.heappop(sticks)
                
            total_cost += temp_cost
            heapq.heappush(sticks, temp_cost)
        
        return total_cost
