class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        dummy = ListNode(0) 
        dummy.next = head
        prev = dummy
        temp = head
        
        while temp:
            if temp.val in seen:
                prev.next = temp.next
            else:
                seen.add(temp.val)
                prev = temp
            temp = temp.next
        
        return dummy.next

