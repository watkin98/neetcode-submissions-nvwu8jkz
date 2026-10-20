# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr_r = head
        while right > 1:
            curr_r = curr_r.next
            right -= 1
        post_r = curr_r.next

        curr_l, prev = head, None
        while left > 1:
            curr_l = curr_l.next
            left -= 1
        pre_l = prev
        curr_r.next = pre_l

        curr, prev = curr_l, post_r
        while curr != pre_l:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev