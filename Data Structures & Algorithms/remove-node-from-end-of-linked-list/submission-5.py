# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        i = 1
        curr = head

        while curr.next:
            curr = curr.next
            i += 1

        curr = head
        n = i - 1
        for _ in range(1, n - 1):
            curr = curr.next
        curr.next = curr.next.next if curr.next else None

        return head
        