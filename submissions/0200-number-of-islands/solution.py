class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
            m, n = len(grid), len(grid[0])

            def valid(r, c):
                return 0 <= r < m and 0 <= c < n

            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            visited = set()

            def dfs(i, j):
                for x, y in directions:
                    next_row, next_col = i + x, j + y
                    if not valid(next_row, next_col):
                        continue
                    if grid[next_row][next_col] == "0":
                        continue
                    if (next_row, next_col) not in visited:
                        visited.add((next_row, next_col))
                        dfs(next_row, next_col)

            ans = 0
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == "1" and (i, j) not in visited:
                        ans += 1
                        visited.add((i, j))
                        dfs(i, j)

            return ans

