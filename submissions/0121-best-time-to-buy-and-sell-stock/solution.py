#  [7,1,5,3,6,4]
#  Output: 5


# [7, 1, 5, 3, 6, 4]
# []

# Edge case:
# When we bought, we cannot sell until our profit could be positive

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def dp(i, bought):
            if i == n:
                return 0
            
            if (i, bought) in memo:
                return memo[(i, bought)]
            
            skip = dp(i + 1, bought)
    
            if bought:
                memo[(i, bought)] = max(skip, prices[i])
            else:
                memo[(i, bought)] = max(skip, -prices[i] + dp(i + 1, True))
    
            return memo[(i, bought)]

        memo = {}
        maxProfit = dp(0, False)
        
        return maxProfit if maxProfit > 0 else 0
