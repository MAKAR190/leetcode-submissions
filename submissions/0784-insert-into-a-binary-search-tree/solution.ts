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

function insertIntoBST(root: TreeNode | null, val: number): TreeNode | null {
    if (!root) {
        return new TreeNode(val); // Create a new node for the empty tree
    }

    let insert = (node) => {
        if (val < node.val) {
            if (!node.left) {
                node.left = new TreeNode(val); // Insert on the left if left is empty
            } else {
                insert(node.left); // Recursively go left
            }
        } else {
            if (!node.right) {
                node.right = new TreeNode(val); // Insert on the right if right is empty
            } else {
                insert(node.right); // Recursively go right
            }
        }
    }

    insert(root); // Start the insertion from the root

    return root; // Return the modified tree
}

