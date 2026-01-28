# Problem definition

# We need to generate as many as possible valid parentheses given the input variable n

# Approach

# Backtracking
# Valid parentheses are closed fully (left==right)
# Store left and right parentheses variable count in each backtracking recusrion frame in order to not generate more parentheses than it is possible and also to check whether the output is valid before backtracking further

# Pseudocode

# Input n=3
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(left, right, curr):
            if len(curr) == 2 * n:
                ans.append("".join(curr[:]))
                return
    
            if left > 0:
                curr.append("(")
                backtrack(left - 1, right, curr)
                curr.pop()
        
            if right > left:
                curr.append(")")
                backtrack(left, right - 1, curr)
                curr.pop()
        
        backtrack(n, n, []) 
        return ans
