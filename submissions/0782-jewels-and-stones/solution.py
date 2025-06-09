from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        countStones = Counter(stones)
        ans = 0
        
        for jewel in jewels:
            if jewel in countStones:
                ans += countStones[jewel]
                
        return ans        
