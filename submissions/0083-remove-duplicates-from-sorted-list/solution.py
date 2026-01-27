# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 -> 2
# curr next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        
        while head and head.next:
            curr = head
            next_node = head.next
            
            if curr.val == next_node.val:
                curr.next = next_node.next
            else:
                curr = curr.next 
            
            head = curr
        
        return dummy
