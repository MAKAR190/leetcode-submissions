from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countsText = Counter(text)
        countsBalloon = Counter("balloon")
        ans = float('inf') 
        
        for ch, count in countsBalloon.items():
            ans = min(ans, countsText[ch] // count if ch in countsText else 0)
        
        return ans

