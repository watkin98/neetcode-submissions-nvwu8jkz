# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2
        res = ListNode()
        head = res

        while ptr1 is not None and ptr2 is not None:
            print(1)
            print(f"ptr1.val <= ptr2.val: {ptr1.val} <= {ptr2.val}")
            if ptr1.val <= ptr2.val:
                print(2)
                temp = ptr1.next
                res.next = ptr1
                ptr1.next = None
                ptr1 = temp
            else:
                print(3)
                temp = ptr2.next
                res.next = ptr2
                ptr2.next = None
                ptr2 = temp

            res = res.next

        if ptr1 is not None:
            res.next = ptr1
        if ptr2 is not None:
            res.next = ptr2

        return head.next