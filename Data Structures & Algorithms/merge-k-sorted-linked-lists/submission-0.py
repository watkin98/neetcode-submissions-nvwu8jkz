# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst_heads = [ListNode()] * len(lists)
        res_head = ListNode()
        curr = res_head

        for i in range(0, len(lists)):
            tracker = lists[i]
            lst_heads[i] = tracker

        # for head in lst_heads:
        #     print(head.val)

        while lst_heads != []:
            lowest_head = lst_heads[0]
            head_tracker = 0

            for i in range(1, len(lst_heads)):
                if lst_heads[i].val < lowest_head.val:
                    lowest_head = lst_heads[i]
                    head_tracker = i

            curr.next = lowest_head
            if lowest_head.next == None:
                del lst_heads[head_tracker]
            else:
                lst_heads[head_tracker] = lst_heads[head_tracker].next

            curr = curr.next
            # print(f"Len: {len(lst_heads)}")
            # break

        return res_head.next