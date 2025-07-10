from collections import deque
from typing import List, Optional

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        level = 0
        
        while queue:
            curr_len = len(queue)
            nodes = []
            
            for _ in range(curr_len):
                node = queue.popleft()
                nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level % 2 == 1:
                nodes.reverse()
            
            ans.append(nodes)
            level += 1
        
        return ans

