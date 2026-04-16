# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head.next

        while f is not None and f.next is not None:
            s = s.next
            f = f.next.next

        list2 = s.next
        s.next = None
        list1 = head

        curr, prev = list2, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        list2 = prev
        
        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            list2.next = temp1
            list1 = temp1
            list2 = temp2

