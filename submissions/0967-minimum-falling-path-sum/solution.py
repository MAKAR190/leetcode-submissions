# Top-down
#from functools import cache
# TC(n * m) SC(m * n (cache))
# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         m, n = len(matrix), len(matrix[0])
#         
#        @cache
#         def dp(row, col):
#             if row == m:
#                 return 0
#             
#             ans = float("inf")
#             next_row = row + 1
#             
#             for next_col in (col - 1, col, col + 1):
#                 if 0 <= next_col < n:
#                     ans = min(ans, matrix[row][col] + dp(next_row, next_col))
#                 
#             return ans
#         
#         return min([dp(0, col) for col in range(n)])

# Bottom-up
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        next_dp = [0] * n
        
        for row in range(m - 1, -1, -1):
            curr_dp = [float("inf")] * n
            for col in range(n):
                for next_col in (col - 1, col, col + 1):
                     if 0 <= next_col < n:
                        curr_dp[col] = min(curr_dp[col], matrix[row][col] + next_dp[next_col])
            next_dp = curr_dp
                    
        
        return min([next_dp[col] for col in range(n)])
