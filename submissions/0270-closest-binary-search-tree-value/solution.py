# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:    
        def dfs(node, ans):
            if not node:
                return ans
            
            if (abs(target - node.val) < abs(target - ans)) or (
                abs(target - node.val) == abs(target - ans) and node.val < ans):
                ans = node.val
        
            if node.val > target:
                return dfs(node.left, ans)
            elif node.val < target:
                return dfs(node.right, ans)
            else:
                return node.val

        
        return dfs(root, root.val)
        
