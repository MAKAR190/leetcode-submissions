# ABCCED

# 4 directions

# matrix - m, n

# begin DFS when finding first letter of the given word

# m, n


# def dfs(r, c)

# for r in m:
#  for c in n:
#  dfs(r,c) if board[r][c] == word[0] 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        letter_freq = {}
        word_freq = {}

        for r in range(m):
            for c in range(n):
                if board[r][c] not in letter_freq:
                    letter_freq[board[r][c]] = 1
                else:
                    letter_freq[board[r][c]] += 1
        
        for x in word:
            if x not in word_freq:
                word_freq[x] = 1
            else:
                word_freq[x] += 1

        for x in word_freq.keys():
            if x not in letter_freq or word_freq[x] > letter_freq[x]:
                return False

        if letter_freq[word[0]] > letter_freq[word[-1]]:
            word = word[::-1]

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n

        def dfs(r, c, i):
            if board[r][c] != word[i]:
                return False

            if i == len(word) - 1:
                return True

            temp = board[r][c]
            board[r][c] = "#"

            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if valid(nx, ny) and dfs(nx, ny, i + 1):
                    board[r][c] = temp
                    return True

            board[r][c] = temp
            return False

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False
