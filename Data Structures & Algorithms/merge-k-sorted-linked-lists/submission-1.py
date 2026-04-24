# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        curr = res

        while lists != []:
            lowest_node = lists[0]
            index = 0

            for i in range(1, len(lists)):
                if lists[i].val < lowest_node.val:
                    lowest_node = lists[i]
                    index = i

            print(f"lowest node: {lowest_node.val}")
            temp = lowest_node.next
            curr.next = lowest_node
            curr = curr.next

            if temp == None:
                print(1)
                lists.pop(index)
            else:
                print(2)
                lists[index] = temp

            #break

        return res.next