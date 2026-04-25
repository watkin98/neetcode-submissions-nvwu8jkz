# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()

        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next

            if list1.val <= list2.val:
                curr.next = list1
                list1.next = None
                list1 = temp1
            else:
                curr.next = list2
                list2.next = None
                list2 = temp2

            curr = curr.next

        if list1 != None:
            curr.next = list1

        if list2 != None:
            curr.next = list2

        return head.next