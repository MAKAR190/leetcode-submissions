# Top-down approach
# from functools import cache
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         
#         @cache
#         def dp(i, holding):
#             if i >= n:
#                 return 0
#             
#             ans = dp(i + 1, holding)
#             
#             if holding:
#                 ans = max(ans, prices[i] + dp(i + 2, False))
#             else:
#                 ans = max(ans, -prices[i] + dp(i + 1, True))
#             
#             return ans
#         
#         return dp(0, False)

# Bottom-up approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for __ in range(2)]  for __ in range(n + 2)]
        
        for i in range(n - 1, -1, -1):
            for j in range(2):
                if j:
                    dp[i][j] = max(dp[i + 1][j], prices[i] + dp[i + 2][0])
                else:
                    dp[i][j] = max(dp[i + 1][j], -prices[i] + dp[i + 1][1])
    
        
        return dp[0][0]
