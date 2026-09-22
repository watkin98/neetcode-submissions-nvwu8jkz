# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        curr = head

        while curr:
            curr = curr.next
            i += 1

        rmvIdx = i - n
        if not rmvIdx:
            return head.next

        curr = head
        for i in range(i - 1):
            if (i + 1) == rmvIdx:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
        