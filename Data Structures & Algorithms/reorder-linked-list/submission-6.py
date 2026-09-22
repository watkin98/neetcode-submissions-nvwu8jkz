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

        curr = slow.next
        slow.next = prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        reverse = prev
        curr = head
        while curr and reverse:
            temp1 = curr.next
            curr.next = reverse
            temp2 = reverse.next
            reverse.next = temp1
            reverse = temp2
            curr = temp1