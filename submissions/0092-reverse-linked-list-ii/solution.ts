/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
   if(!head || left === right){
       return head;
   }
    
   let dummy = new ListNode(0);
    dummy.next = head;
    let prev = dummy;
    
    for (let i = 1; i < left; i++){
        prev = prev.next;
    }
    
    let curr = prev.next;
    let nextNode;
    
    for (let i = left; i < right; i++){
        nextNode = curr.next;
        curr.next = nextNode.next;
        nextNode.next = prev.next;
        prev.next = nextNode;
    }
    return dummy.next;
};
