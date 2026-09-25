# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        carry = 0
        place = 0

        while l1 and l2:
            curSum = l1.val + l2.val + carry

            if curSum > 9:
                curSum %= 10
                carry = 1
            else:
                carry = 0
            #print(curSum)
            total += curSum * int(math.pow(10, place))
            place += 1

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total += l1.val * int(math.pow(10, place))
            place += 1
            l1 = l1.next
        while l2:
            total += l2.val * int(math.pow(10, place))
            place += 1
            l2 = l2.next

        if carry:
            total += int(math.pow(10, place))
            place += 1
        
        # print()
        # print(total)
        # print(place)
        head = curr = ListNode(-1)
        for i in range(place - 1, -1, -1):
            val = total // int(math.pow(10, i))
            node = ListNode(val)
            curr.next = node
            curr = curr.next
            total -= val * int(math.pow(10, i))

        head = head.next
        curr, prev = head, None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

