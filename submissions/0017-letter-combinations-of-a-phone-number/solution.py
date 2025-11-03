class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        
        def backtrack(curr, i):
            if len(curr) == len(digits):
                ans.append(curr[:])
                return
            
            for letter in digit_letters[digits[i]]:
                curr += letter
                backtrack(curr, i + 1)
                curr = curr[:-1]
                
        ans = []
        backtrack("", 0)
        return ans
