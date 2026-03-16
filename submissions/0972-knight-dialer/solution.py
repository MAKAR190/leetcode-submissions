class Solution:
    def knightDialer(self, n: int) -> int:
        total = 0
        MOD = 10 ** 9 + 7
        dialer = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]
        knight_jumps = [(2, 1), (2, -1), (1, -2), (1, 2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
        rows, cols = len(dialer), len(dialer[0])

        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols and dialer[r][c].isdigit()

        def dp(i, j, curr):
            if curr == n:
                return 1

            if (i, j, curr) in memo:
                return memo[(i, j, curr)]

            total = 0
            for jump_y, jump_x in knight_jumps:
                new_r, new_c = i + jump_y, j + jump_x
                if valid(new_r, new_c):
                    total += dp(new_r, new_c, curr + 1)
            
            memo[(i, j, curr)] = total % MOD
            return memo[(i, j, curr)]

        memo = {}

        for i in range(rows):
            for j in range(cols):
                if dialer[i][j].isdigit():
                    total += dp(i, j, 1)

        return total % MOD
