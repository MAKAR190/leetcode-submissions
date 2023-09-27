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

function zigzagLevelOrder(root: TreeNode | null): number[][] {
 
    if (!root) {
      return [];
    }
    
    let result = []
    let isReverse = true
    let queue = [root]
    
    while (queue.length) {
        let currentLevelLength = queue.length;
         let newQueue = [];
        
        for (let i = 0; i < currentLevelLength; i++){
            let node = queue.shift();
            newQueue.push(node.val)
           
            if(node.right){
                queue.push(node.right)
            }
            if(node.left){
                queue.push(node.left)
                
            }
           
        }
     
         if (isReverse) {
            newQueue.reverse();
        }
            
            result.push(newQueue)
        isReverse = !isReverse
    }
    return result;
};
