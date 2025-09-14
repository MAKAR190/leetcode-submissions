# Define the problem

# So the problem lies in finding a border (exit) from the entrance (row, col) using 4-directional approach, which 
# are the neighbours of current node. The exit cannot be the entrance, it should be a border. The border is the 
# node with at least one step outside the boundaries of the maze. The wall neighbour is '+' and an empty  
# neighbour is '.'

# Approach

from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(r, c):
            return  0 <= r < m and 0 <= c < n and maze[r][c] == "."
         
        def exit(r, c):
            return r == 0 or r == m - 1 or c == 0 or c == n - 1
        
        m, n = len(maze), len(maze[0])
        directions = {(0, 1), (0, -1), (-1, 0), (1, 0)}
        seen = {(entrance[0], entrance[1])}
        queue = deque([(entrance[0], entrance[1], 0)])        
  
        while queue:
            curr_len = len(queue)
            
            for _ in range(curr_len):
                r, c, steps = queue.popleft()
                
                for dx, dy in directions:
                    next_r, next_c = r + dx, c + dy
                    
                    if valid(next_r, next_c) and (next_r, next_c) not in seen:
                        
                        if exit(next_r, next_c):
                            return steps + 1
                        
                        
                        seen.add((next_r, next_c))
                        queue.append([next_r, next_c, steps + 1])
        
        return -1
