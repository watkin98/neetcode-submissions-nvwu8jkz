# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # advance one pointer n positions in the list
        ptr1 = head
        while n > 0:
            ptr1 = ptr1.next
            n -= 1

        # advance two other pointers until ptr1 is None
        curr, prev = head, None
        while ptr1:
            prev = curr
            curr = curr.next
            ptr1 = ptr1.next

        # prev pointer's next pointer points to the node we wish to remove
        if prev != None:
            prev.next = prev.next.next
        else:
            head = None

        return head
