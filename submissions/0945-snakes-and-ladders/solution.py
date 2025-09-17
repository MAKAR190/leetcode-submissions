### My algo pseudo solution

# Start at cell 1 (board[n - 1][0]). Board size is n^2. 
# I need to write a func which will convert square number to (row, col)
# Setup variables: board len, seen, queue
# Simulate game moves through queue and graph BFS, the fastest one which will reach the finish -> return moves + 1
#  while queue:
#       n = length_queue
#       
#       for square in queue:
#           square, moves = queue.pop() 
#           
#           for next in range(square + 1, square + 6):
#               if next == n^2:
#                      return moves + 1
#               
#               next_square_val = convert(next)
#
#               if next_square_val != -1 and not in seen next_square_val:
#                      seen.add(next_square_val)
#                      queue.add((next_square_val, moves + 1))
#               elif not in seen next: 
#                      seen.add(next)
#                      queue.add((next, moves + 1))
#
#  return -1
#
#
# Challenge: susbsequent ladder or snake ??? - solved with seen I quess
# SIUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU FIRST MEDIUM BABABABYYYYYYYYYYYYYY

from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def board_value(square):
            row_base = (square - 1) // n  
            row = n - 1 - row_base 
            col = square - n * row_base - 1 if row_base % 2 == 0 else n * (row_base + 1) - square
            
            return board[row][col]
                            
        
        start_square = 1
        
        n = len(board)     
        seen = {start_square} 
        queue = deque([(start_square, 0)]) # 0 moves
        
        while queue:
            curr_length = len(queue)
       
            for _ in range(curr_length):
                square, moves = queue.popleft()
           
                for next_square in range(square + 1, min(square + 6, n**2) + 1):
                    next_square_val = board_value(next_square) 
                    next_square_val = board_value(next_square) if next_square_val != -1 else next_square

                    if next_square_val == n**2:
                        return moves + 1
                    
                    if next_square_val not in seen:
                        seen.add(next_square_val)
                        queue.append((next_square_val, moves + 1))
        
        return -1
        
