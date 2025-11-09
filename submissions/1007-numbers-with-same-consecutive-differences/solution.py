# Defining the problem
# We need to generate all possible n-length integers with k-distance between digits. 
# The only way of validating integer length is through converting it into the string or splitting into array. In my opinion, we could store them in the array curr, and append into the answer after reaching length n.
# But this is only the base case handling, so the main question - is how do we manage to generate all possible integers in the most optimized way? 

# 
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(curr):
            if len(curr) == n:
                ans.append(int("".join(list(map(str, curr)))))
                return 
            
            for i in range(0, 10):
                if len(curr) == 0 and i == 0:
                    continue
                    
                if len(curr) == 0 or abs(curr[-1] - i) == k:
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()
                
        ans = []
        backtrack([])
        return ans
