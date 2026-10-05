# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list2 = slow.next
        slow.next = None

        curr, prev = list2, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        list1, list2 = head, prev
        while list1 and list2:
            temp1 = list1.next
            list1.next = list2
            temp2 = list2.next
            list2.next = temp1

            list1, list2 = temp1, temp2
        