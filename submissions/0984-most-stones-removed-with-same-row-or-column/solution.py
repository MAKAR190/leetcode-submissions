# 2D plane, n stones at some coordinate point integers

# Each row and column should have at least one stone before any stone from this row or column can be removed

# [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

# output - the largest possible number of stones that can be removed.

# n <= 10 ** 3 TTL <= 10 ** 6 <= 10 ** 8 or 10 ** 9

# Constrained stone removal based on curr: row, col

# We model each node in this graph as a stones, and they are connected, when they share a row or a col. Each connected component can be reduced to one stone, which means the resul is total stones minus the number of components


# Rows:
# 0: [0, 2]
# 1: [1]
# 2: [0, 2]

#Cols:
# 0: [0]
# 1: [1]
# 2: [2]

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        from collections import defaultdict

        n = len(stones)

        row_map = defaultdict(list)
        col_map = defaultdict(list)

        for i, (x, y) in enumerate(stones):
            row_map[x].append(i)
            col_map[y].append(i)
        
        visited = set()
        
        def dfs(i):
            stack = [i]
            visited.add(i)

            while stack:
                curr = stack.pop()
                x, y = stones[curr]

                # same row
                for nei in row_map[x]:
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)

                # same column
                for nei in col_map[y]:
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)

        components = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return n - components
        
