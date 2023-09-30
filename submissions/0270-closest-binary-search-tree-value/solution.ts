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

function closestValue(root: TreeNode | null, target: number): number {
        const inorder = (r: TreeNode | null): number[] => {
            return r ? [...inorder(r.left), r.val, ...inorder(r.right)] : [];
        };

        const values = inorder(root);
        return values.reduce((closest, x) => Math.abs(target - x) < Math.abs(target - closest) ? x : closest, values[0]);
    }
