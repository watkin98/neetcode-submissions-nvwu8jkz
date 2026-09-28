# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the list
        slow, fast = head, head.next
        #slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half of the list
        curr, prev = slow if not fast else slow.next, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # append nodes from each list in order
        list1, list2 = head, prev
        print(list1.val)
        print(list2.val)
        
        while list1 and list2:
            temp1 = list1.next
            list1.next = list2
            list1 = temp1

            temp2 = list2.next
            list2.next = list1
            list2 = temp2
        if list1:
            list1.next = None