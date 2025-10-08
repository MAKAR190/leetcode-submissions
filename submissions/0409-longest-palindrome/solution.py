# Problem

# Input: s = "abbccccddddd"
# 1* a -> 2 * b -> 4 * c -> 5 * d
# 4 unique letters

#    ....dccaccd.....

# Approach
# 1. 
# 2. 
# 3. 

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_count = Counter(s)
        ans = 0
        has_odd_frequency = False

        for char, count in s_count.items():
            if count % 2 == 0:
                ans += count
            else:
                ans += count - 1 
                has_odd_frequency = True

        if has_odd_frequency:
            return ans + 1
        return ans

