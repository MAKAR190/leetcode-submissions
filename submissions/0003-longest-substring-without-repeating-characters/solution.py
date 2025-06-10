class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        un_chars = set()
        left = 0
        ans = 0
        
        for right in range(len(s)):
            while s[right] in un_chars:
                un_chars.remove(s[left])
                left += 1
            un_chars.add(s[right])
            ans = max(ans, right - left + 1)
        
        return ans

