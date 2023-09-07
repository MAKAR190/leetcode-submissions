/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function maxAncestorDiff(root: TreeNode | null): number {
    if (!root) {
        return 0;
    }

    function dfs(node, minSoFar, maxSoFar) {
        if (!node) {
            return maxSoFar - minSoFar;
        }

        minSoFar = Math.min(minSoFar, node.val);
        maxSoFar = Math.max(maxSoFar, node.val);

        const leftDiff = dfs(node.left, minSoFar, maxSoFar);
        const rightDiff = dfs(node.right, minSoFar, maxSoFar);

        return Math.max(leftDiff, rightDiff);
    }

    return dfs(root, root.val, root.val);
};
