# Top-down approach
# from functools import cache
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m, n = len(obstacleGrid), len(obstacleGrid[0])
#         
#         @cache
#         def dp(row, col):
#             if obstacleGrid[row][col] == 1:
#                 return 0
#             
#             if row + col == 0:
#                 return 1
#             
#             up = dp(row - 1, col) if row > 0  else 0
#             left = dp(row, col - 1) if col > 0 else 0
#         
#             return up + left
#         
#         return dp(m - 1, n - 1)

# Bottom-up approach
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m, n = len(obstacleGrid), len(obstacleGrid[0])
#         dp = [[0 for __ in range(n)] for __ in range(m)]
#         dp[0][0] = 1
#         
#         for row in range(m):
#             for col in range(n):
#                 if obstacleGrid[row][col] == 1:
#                     dp[row][col] = 0
#                     continue
#                 
#                 if row > 0:
#                      dp[row][col] += dp[row - 1][col]
#                 
#                 if col > 0:
#                     dp[row][col] += dp[row][col - 1]
#         
#         return dp[m - 1][n - 1]

# Bottom-up approach (improved space complexity to just O(n))
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1
        
        for row in range(m):
            next_row = [0] * n
            for col in range(n):
                next_row[col] = dp[col]
                
                if obstacleGrid[row][col] == 1:
                    next_row[col] = 0
                    continue
                
                if col > 0:
                    next_row[col] += next_row[col - 1]
                
            
            dp = next_row
        
        return dp[n - 1]
