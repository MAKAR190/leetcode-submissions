from collections import defaultdict
from heapq import *

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        
        for x, y, z in flights:
            graph[x].append([y, z])
        
        distances = [[float('inf') for __ in range(k + 2)] for __ in range(n)]
        distances[src][0] = 0
        
        heap = [(0, src, 0)] 
        
        while heap:
            curr_dist, city, stops = heappop(heap)
            
            if curr_dist > distances[city][stops]:
                continue
            
            for neighbor, price in graph[city]:
                next_stops = stops + 1
                if next_stops <= k + 1:
                    new_cost = curr_dist + price
                    if new_cost < distances[neighbor][next_stops]:
                        distances[neighbor][next_stops] = new_cost
                        heappush(heap, (new_cost, neighbor, next_stops))
        
        ans = min(distances[dst][1:k+2])
        return -1 if ans == float('inf') else ans
