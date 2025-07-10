# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        last_level = []
        
        while queue:
            curr_len = len(queue)
            last_level = []
            
            for _ in range(curr_len):
                node = queue.popleft()
                last_level.append(node.val) 

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return sum(last_level)  
                
