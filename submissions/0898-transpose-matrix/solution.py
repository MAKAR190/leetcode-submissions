class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = [[] for i in range(n)]

        for i in range(n):
                curr_col = [matrix[col_num][i] for col_num in range(m)]
                ans[i] = curr_col

        return ans
