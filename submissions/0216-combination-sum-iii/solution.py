class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(curr_nums, curr_sum, j):
             if len(curr_nums) == k and curr_sum == n:
                ans.append(curr_nums[:])
                return
    
             for i in range(j, 10):
                if curr_sum + i <= n and len(curr_nums) < k:
                    curr_nums.append(i)
                    backtrack(curr_nums, curr_sum + i, i + 1)
                    curr_nums.pop()
             
        
        ans = []
        backtrack([], 0, 1)
        return ans
