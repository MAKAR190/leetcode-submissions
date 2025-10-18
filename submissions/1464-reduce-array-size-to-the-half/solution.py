import math
import heapq

# Bucker sort instead of timsort or heap approaches (which are O(n+klogk)) and bucker sort is O(n)

from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = {}
        max_frequency = 0
        
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > max_frequency:
                max_frequency = counts[num]
                
        ans = 0
        removed_length = 0
        
        buckets = [0] * (max_frequency + 1)
        
        for count in counts.values():
            buckets[count] += 1
        
        for freq in range(max_frequency, 0, -1):
            while buckets[freq] > 0 and removed_length < math.ceil(len(arr) / 2):
                ans += 1
                removed_length += freq
                buckets[freq] -= 1
                
        return ans
