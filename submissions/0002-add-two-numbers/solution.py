# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 2 -> 4 -> 3
# 5 -> 6 -> 4

# 3 -> 4 -> 2
# 4 -> 6 -> 5

# 9 -> 9 -> 9
# 1 -> 5

# 0 -> 5 -> 0 -> 1


# Edge cases
# 1. We do need to add another digit postion 
# 2. We need to remember carry and add to the next digit
# 3. Lengths of linked lists are not the same

# 1. Reverse l2
# 2. Start adding digits (we don't want to forget about carry) 
# 3. Store the result in a new linked list
# Retur

# Pseucode
# Input: l1, l2

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result_head = None
        
        while l1 and l2:
            digits_sum = l1.val + l2.val + carry
            carry = digits_sum // 10
            
            if not result_head:
                result_head = ListNode(digits_sum % 10)
                dummy = result_head
            else:
                result_head.next = ListNode(digits_sum % 10)
                result_head = result_head.next
                
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            digits_sum = l1.val + carry
            carry = digits_sum // 10
            result_head.next = ListNode(digits_sum % 10)
            
            result_head = result_head.next
            l1 = l1.next
            
        while l2:
            digits_sum = l2.val + carry
            carry = digits_sum // 10
            result_head.next = ListNode(digits_sum % 10)
            
            result_head = result_head.next
            l2 = l2.next
            
        if carry:
            result_head.next = ListNode(carry)
            result_head = result_head.next
        
        return dummy
