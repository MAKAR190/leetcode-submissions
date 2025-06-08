from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance_index_map = {0: -1}  
        max_length = 0
        balance = 0
        
        for i, num in enumerate(nums):
            balance += 1 if num == 1 else -1
            
            if balance in balance_index_map:
                max_length = max(max_length, i - balance_index_map[balance])
            else:
                balance_index_map[balance] = i
        
        return max_length

