class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or (row, col) in seen or grid[row][col] == 0:
                return 0
             
            seen.add((row, col))    
            area = 1  
            for dx, dy in directions:
                area += dfs(row + dx, col + dy)
            
            return area
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in seen and grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area
