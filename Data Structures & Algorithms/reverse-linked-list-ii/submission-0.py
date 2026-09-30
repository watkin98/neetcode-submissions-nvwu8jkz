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
        tmp = leftPortion
        leftPortion = leftPortion.next
        i = 0
        rightPortion = dummy
        while i < right:
            rightPortion = rightPortion.next
            i += 1
        rightPortion = rightPortion.next

        # print(leftPortion.val)
        # print(rightPortion.val)
        curr, prev = leftPortion, rightPortion
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        tmp.next = prev
        return dummy.next
