# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr, prev = slow.next, None
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr1, curr2 = head, prev
        while curr1 and curr2:
            tmp1 = curr1.next
            tmp2 = curr2.next

            curr1.next = curr2
            curr2.next = tmp1

            curr1 = tmp1
            curr2 = tmp2
