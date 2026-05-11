# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        curr = res

        while len(lists) != 0:
            smallest_node, index = lists[0], 0

            for i, node in enumerate(lists): # can this loop's starting i be changed?
                if node.val < smallest_node.val:
                    smallest_node = node
                    index = i

            curr.next = smallest_node
            lists[index] = lists[index].next
            curr = curr.next

            if lists[index] == None:
                del lists[index]

        return res.next

        