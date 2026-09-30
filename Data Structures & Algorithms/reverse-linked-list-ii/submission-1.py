# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        i = 1
        leftPortion = dummy
        while i < left:
            leftPortion = leftPortion.next
            i += 1
        start = leftPortion.next

        i = 0
        rightPortion = dummy
        while i < right:
            rightPortion = rightPortion.next
            i += 1
        rightPortion = rightPortion.next

        curr, prev = start, rightPortion
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        leftPortion.next = prev
        return dummy.next
