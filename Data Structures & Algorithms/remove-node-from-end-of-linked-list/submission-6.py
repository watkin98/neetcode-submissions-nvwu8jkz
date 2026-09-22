# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        curr, prev = head, None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        i = 1
        head = prev
        curr, prev = head, None

        while curr:
            if i == n:
                break
            prev = curr
            curr = curr.next
            i += 1

        prev.next = prev.next.next if prev.next else None

        curr, prev = head, None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev