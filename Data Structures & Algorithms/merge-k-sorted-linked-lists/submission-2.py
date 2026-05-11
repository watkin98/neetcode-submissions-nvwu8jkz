# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        k = 0
        # iterate through lists until len(lists) == 0
        while len(lists) != 0:
            #if k == 2:
            #    break
            # store the first node in a smallest_node var
            smallest_node, index = lists[0], 0
            # iterate through each list in lists, checking the head node
            # and comparing the node with smallest_node
                # if head node < smallest_node, update smallest node
            for i, node in enumerate(lists): # can this loop's starting i be changed?
                if node.val < smallest_node.val:
                    smallest_node = node
                    index = i
            # append the smallest node to the res linked list and update the 
            # smallest node's old linked list
                # if the old linked list is empty, remove its reference from lists
            curr.next = smallest_node
            lists[index] = lists[index].next
            print(lists[index])
            curr = curr.next

            if lists[index] == None:
                del lists[index]
                print(lists)
            #k += 1

        return res.next

        