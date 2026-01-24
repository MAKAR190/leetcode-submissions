# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem Definition
# We need to replace the entire right subtree with left one for each parent node
# We update our binray tree starting from roo in-place just using recusrion really, which will use the stack under the hood

# Edge case
# Root is empty
# Parent node has only one child

# Approach
# 1. DFS
# 2. Repoint parent node from right node to left for each parent node
# 3. Return the root because it won't change


# Pseudocode

#if not root:
#    return None

#left = dfs(root.left)
#right = dfs(root.right)

#root.left = right
#root.right = left

#return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
       
        root.left = right
        root.right = left

        return root
