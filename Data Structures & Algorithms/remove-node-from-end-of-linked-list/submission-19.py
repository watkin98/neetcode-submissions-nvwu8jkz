# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        
        curr = head
        while n > 0:
            curr = curr.next
            n -= 1

        prev = dummy
        while curr:
            curr = curr.next
            prev = prev.next

        prev.next = prev.next.next #if prev.next else None

        return dummy.next