class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        def dp(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            if remaining in memo:
                return memo[remaining]
    
           
            best = float("inf")
            for coin in coins:
                best = min(best, 1 + dp(remaining - coin))

            memo[remaining] = best
            return best
    

        memo = {}
        ans = dp(amount)
        
        return ans if ans != float('inf') else -1
