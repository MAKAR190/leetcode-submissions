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

function deepestLeavesSum(root: TreeNode | null): number {
  if(!root){
     return 0;
  }
  
  let ans:number = 0;
  let queue = [root]
  
  while(queue.length){
     let lengthOfCurrentLevel = queue.length;
     let nextQueue = [];
      
     for (let i = 0; i < lengthOfCurrentLevel; i++) {
         
         let node = queue[i];
         
         if(node.left){
            nextQueue.push(node.left) 
         }
         if(node.right){
             nextQueue.push(node.right)
         } else if(!nextQueue.length){
             ans = queue.reduce((acc, el)=>acc+=el.val, 0);
         }
     }
     queue = nextQueue 
  }

    return ans;
};
