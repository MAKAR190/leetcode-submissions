# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#   3 
#  / \ 
# 1   4
#  \
#   2
 
# Edge cases
# 1. We don't have any negatives 

# Approach

# 1. Start DFS from the root
# 2. Use a heap each time to either insert or pop an element if it is more than current node's value based on heap length which is at most k
# 3. Return the top element from the heap, which would be the k-th smallest element in BST

# TC(O(n * log k)) SC(O(n + k))

# This is a first brute-force solution which is not using BST logic and not optimal. Let's do an optimal one

# Using in-order approach in BST, we will always have a sorted order from smallest to largest integers. So we just stop counting at k-th from in-order, and return it.

# SC(O(h)) TC(O(k))


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = curr = 0

        def dfs(node):
            nonlocal curr, ans
            if not node or curr >= k:
                return
            
            dfs(node.left)
            curr += 1
            if curr == k:
                ans = node.val
                return

            dfs(node.right)

        dfs(root)
        return ans  

