class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)        # Dummy head node
        self.tail = self.head.next
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next

        while curr and i < index:
            curr = curr.next
            i += 1

        return curr.val if i == index else -1

    def insertHead(self, val: int) -> None:
        self.head.next = Node(val, self.head.next)
        if self.tail == None:
            self.tail = self.head.next

    def insertTail(self, val: int) -> None:
        if self.tail != None:
            self.tail.next = Node(val)
        else:
            self.insertHead(val)

    def remove(self, index: int) -> bool:
        i = 0
        prev = self.head
        curr = self.head.next

        while curr and i < index:
            prev = curr
            curr = curr.next

        print(prev.val)
        print(curr.val)
        print(curr.next.val)
        if i == index:
            prev.next = curr.next
            return True
        else:
            return False


    def getValues(self) -> List[int]:
        nums = []
        curr = self.head.next

        while curr:
            nums.append(curr.val)
            curr = curr.next

        return nums
