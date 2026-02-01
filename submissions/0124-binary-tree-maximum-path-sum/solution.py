# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#   1
# 2   3

# Edge cases
# 1. Our root can be empty

# Approach

# 1. Start DFS from root
# 2. For each dfs call, call internal DFS function which returns maximum sum path for current node
# 3. Store the result for each internal DFS call in the maximum answer variable
# 4. We handle duplicates by going down on each internal DFS call
# 5. TC(O(n*n)) SC(O(n))

#               5
#            4     8
#          11    13  4
#        7   2         1


# Optimilized from O(n**2) to O(n) by computing the final answer on the fly


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = root.val

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            ans = max(ans, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return ans
