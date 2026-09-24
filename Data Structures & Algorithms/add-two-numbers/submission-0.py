# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_stack = []
        l2_stack = []

        curr = l1
        while curr:
            l1_stack.append(str(curr.val))
            curr = curr.next

        curr = l2
        while curr:
            l2_stack.append(str(curr.val))
            curr = curr.next

        num1 = int("".join(l1_stack[::-1]))
        num2 = int("".join(l2_stack[::-1]))
        res = num1 + num2
        
        res = str(res)[::-1]    
        dummy = curr = ListNode(-1)

        for num in res:
            node = ListNode(int(num))
            curr.next = node
            curr = curr.next
        
        return dummy.next