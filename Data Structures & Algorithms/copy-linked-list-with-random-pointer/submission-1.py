"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_pairs = {}
        curr = head

        while curr:
            new_node = Node(curr.val)
            node_pairs[curr] = new_node
            curr = curr.next

        new_head = new_curr = Node(-101)
        curr = head
        while curr:
            new_curr.next = node_pairs[curr]
            new_curr = new_curr.next

            new_curr.next = node_pairs[curr.next] if curr.next else None
            new_curr.random = node_pairs[curr.random] if curr.random else None

            curr = curr.next

        return new_head.next
