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

function diameterOfBinaryTree(root: TreeNode | null): number {
   if(!root){
       return 0;
   }
    
   function height(node){
     if(!node){
         return 0;
     }
     return Math.max(height(node.left), height(node.right)) + 1;  
   } 
    
   function callTheDiameter(node){
       
     if(!node){
         return 0;
     }  
     
     let leftHeight = height(node.left);
     let rightHeight = height(node.right);
      
     let diameterThroughNode = leftHeight + rightHeight;
       
     let leftDiameter = callTheDiameter(node.left);
      let rightDiameter = callTheDiameter(node.right);
       
     return Math.max(diameterThroughNode, leftDiameter, rightDiameter);  
       
   }
    return callTheDiameter(root);
 
};
