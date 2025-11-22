# Defining the problem
# So we need to use infinite number of coins of those which we can access (denominations array) to sum up them to amount and return the fewest possible amount of coins needed. If we cannot do that -- return -1

# TC and SC
#

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(a): 
            if a == 0:
                return 0
            
            if a < 0: return float('inf')
            
            if a in memo:
                return memo[a]
            
            memo[a] = min(dp(a - c) + 1 for c in coins)
            return memo[a]
        
        memo = {}
        ans = dp(amount)
        return -1 if ans == float('inf') else ans
