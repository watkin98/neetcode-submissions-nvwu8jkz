class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)        # Dummy head node
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next

        while curr and i < index:
            curr = curr.next
            i += 1

        return curr.val if curr and i == index else -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val, self.head.next)
        self.head.next = newNode
        if self.tail == self.head:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        i = 0
        prev = self.head
        curr = self.head.next

        while curr and i < index:
            prev = curr
            curr = curr.next
            i += 1

        if curr and i == index:
            if curr == self.tail:
                self.tail = prev
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