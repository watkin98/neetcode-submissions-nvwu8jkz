# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Recursion Contract: given a node and the previous node, this
        # helper swaps in-place the position of the node and its child.
        # Smaller subproblem: swaps itself with its direct child and calls itself 
        # on its grandchild before returning.
        # Progress: each call traverses the linked list.
        # Base Case: When node is None or its child is None, return.
        # Use of Child Result: None
        def swap(node, prev):
            if node is None or node.next is None:
                return

            temp = node.next.next
            prev.next = node.next
            node.next.next = node
            node.next = temp

            swap(node.next, node)

        sentinel = ListNode(-1, head)
        swap(head, sentinel)

        return sentinel.next
  

