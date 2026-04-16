# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        # if n == 1:
        #     curr, prev = head, None
        #     while curr.next:
        #         prev = curr
        #         curr = curr.next

        #     prev.next = None
        #     return head

        curr, prev = head, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        new_head = prev
        curr = new_head
        prev = curr

        if n == 1:
            new_head = new_head.next
        else:
            for i in range(1, n):
                prev = curr
                curr = curr.next

            prev.next = curr.next

        curr, prev = new_head, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev



        
