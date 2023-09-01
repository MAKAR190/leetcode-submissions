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

function deleteDuplicates(head: ListNode | null): ListNode | null {
   let dummy = head;
   
   if(dummy === null){
       return null;
   }
   
    while(dummy && dummy.next){
        if(dummy.val === dummy.next.val){
            dummy.next = dummy.next.next
        } else{
            dummy = dummy.next;
        }
    }
    
    return head;
};
