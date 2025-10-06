# QUESTIONS
# Anagram - UNDERSTOOD
# s and t consist of lowercase English letters. (s and S wouldn't be an edge case beacuse of this constraint)
# about this follow-up - in Python 3 all strings are unicode by default so we don't need to normalise them in case when two different systems could use different UTF bases and could mess up unicode characters
# EDGE CASE - two strings must be the same length if they are anagrams


# Suggested approach (or brute force one)
# We use hashmap to count and then compare


# TC and SC
# TC(s + t) SC(s + t)

# Debugging before testing

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict, t_dict = Counter(s), Counter(t)

        for key, val in s_dict.items():
            if key not in t_dict or t_dict[key] != val:
                return False

        return True    

    
