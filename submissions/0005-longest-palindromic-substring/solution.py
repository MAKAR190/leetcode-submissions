class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = {}

        def dfs(i, j):
            if i >= j:
                return True

            if s[i] != s[j]:
                return False
                
            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = s[i] == s[j] and dfs(i+1, j-1)
            return memo[(i, j)]

        ans = ""

        for i in range(n):
            for j in range(i, n):
                if dfs(i, j) and j - i + 1 > len(ans):
                    ans = s[i:j+1]

        return ans
            

