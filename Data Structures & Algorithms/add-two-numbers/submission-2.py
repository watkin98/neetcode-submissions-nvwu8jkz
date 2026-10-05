# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = curr = ListNode(-1)

        carry = 0
        while l1 and l2:
            total = l1.val + l2.val
            total += carry
            
            if total > 9:
                total %= 10
                carry = 1
            else:
                carry = 0

            curr.next = ListNode(total)
            curr = curr.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            total = l1.val + carry

            if total > 9:
                total = 0
                carry = 1
            else:
                carry = 0
            
            curr.next = ListNode(total)
            curr = curr.next
            l1 = l1.next

        while l2:
            total = l2.val + carry

            if total > 9:
                total = 0
                carry = 1
            else:
                carry = 0
            
            curr.next = ListNode(total)
            curr = curr.next
            l2 = l2.next
        
        if carry:
            curr.next = ListNode(1)

        return res.next