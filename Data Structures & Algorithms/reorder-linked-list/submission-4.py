# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #split the list into halves
        slow = head
        fast = head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next


        lst1 = head
        lst2 = slow.next
        slow.next = None

        # print(f"lst1: {lst1.val}")
        # print(f"lst2: {lst2.val}")
        #reverse the second half
        curr, prev = lst2, None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # while prev:
        #     print(f"reversed val: {prev.val}")
        #     prev = prev.next

        #append alternating nodes from each list into one linked list
        lst2 = prev
        
        curr1, curr2 = lst1, lst2
        while curr1 != None and curr2 != None:

            temp1 = curr1.next
            temp2 = curr2.next
            print("Before:")
            print(f"c1: {curr1.val}\nc2: {curr2.val}")
            #print(f"t1: {temp1.val}\nt2: {temp2.val}")

            curr1.next = curr2
            curr2.next = temp1

            curr1 = temp1
            curr2 = temp2
            print("After:")
            #print(f"c1: {curr1.val}\nc2: {curr2.val}")



