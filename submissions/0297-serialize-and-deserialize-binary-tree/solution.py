# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root) -> str:
        ans = []

        def dfs(node):
            if not node:
                ans.append("#")
                return

            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(ans)

    def deserialize(self, data) -> TreeNode:
        processed = data.split(",")
        n = len(processed)
        idx = -1

        def create_tree() -> TreeNode:
            nonlocal idx
            idx += 1

            if idx >= n:
                return None

            if processed[idx] == "#":
                return None

            node = TreeNode(int(processed[idx]))
            node.left = create_tree()
            node.right = create_tree()
            return node

        return create_tree()

