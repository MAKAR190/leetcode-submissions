class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = {}
        n = len(s)
        left = ans = 0
        
        for right in range(n):
            ch = s[right]
            counts[ch] = counts.get(ch, 0) + 1
            
            while counts[ch] > 1:
                counts[s[left]] -= 1
                
                if counts[s[left]] == 0:
                    del counts[s[left]]
                
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
