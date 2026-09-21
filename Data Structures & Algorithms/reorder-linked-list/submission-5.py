# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        l, r = 1, len(nodes) - 1
        new_list = curr = head
        
        while l < r:
            curr.next = nodes[r]
            nodes[r].next = nodes[l]
            l += 1
            r -= 1
            curr = curr.next.next
        if l == r:
            curr.next.next = None
        else:
            curr.next = None