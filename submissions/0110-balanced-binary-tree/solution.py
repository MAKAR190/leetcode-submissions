# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            height_left = dfs(node.left) if node.left else 0
            if height_left == -1:
                return -1

            height_right = dfs(node.right) if node.right else 0
            if height_right == -1:
                return -1

            if abs(height_left - height_right) > 1:
                return -1

            return 1 + max(height_left, height_right)
            
        if not root:
            return True
        
        return dfs(root) != -1
