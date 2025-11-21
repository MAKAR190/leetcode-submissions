# Problem definition
# We need to calculate the minimum cost to reach to the top, which means after each step to choose next minimal step, which can be either one or two steps ahead. 

# Base cases
# dp(0) == dp(1) == 0

# State function
# Our state function recieves and index of current staircase, so to decide the next one or to reach the top and add minimal cost to total cost. We also need to memoize this function in order to recieve linear time complexity

# Recurrence relation
# Only do if i is not out of range
# cost = min(dp(i + 1) + cost[i], dp(i + 2) + cost[i])

# Approach
# DP - top-down -> bottom-up


# Top-down approach
# TC and SC
# TC(n) SC(n)
# class Solution:
#    def minCostClimbingStairs(self, cost: List[int]) -> int:
#        def dp(i):
#            if i <= 1:
#                return 0
#
#            if i in memo:
#                return memo[i]
#            
#            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
#            return memo[i]
#        
#        memo = {}
#        return dp(len(cost))
    
# Bottom-up approach   
# TC and SC
# TC(n) SC(n)
# class Solution:
#    def minCostClimbingStairs(self, cost: List[int]) -> int:
#        dp = [0] * (len(cost) + 1)
#        
#        for i in range(2, len(cost) + 1):
#            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
#   
#        return dp[len(cost)]

# Bottom-up approach   
# TC and SC
# TC(n) SC(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = 0, 0
        
        for i in range(2, len(cost) + 1):
            curr = min(prev1 + cost[i-1], prev2 + cost[i-2])
            prev2, prev1 = prev1, curr
        return prev1        
