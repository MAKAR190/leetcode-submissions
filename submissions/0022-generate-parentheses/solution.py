class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, left, right):
            if len(curr) == 2 * n:
                ans.append(curr[:])
                return
            
            if left < n:
                curr += "("
                backtrack(curr, left + 1, right)
                curr = curr[:-1]
            
            if left > right:
                curr += ")"
                backtrack(curr, left, right + 1)
                curr = curr[:-1]
        
        ans = []
        backtrack("", 0, 0)
        return ans
