# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)

        rightNode = dummy
        while right > 0:
            rightNode = rightNode.next
            right -= 1
        nextRight = rightNode.next
        rightNode.next = None

        leftNode, prevLeft = dummy, None
        while left > 0:
            prevLeft = leftNode
            leftNode = leftNode.next
            left -= 1

        curr, prev = leftNode, nextRight
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        prevLeft.next = prev

        return dummy.next
        