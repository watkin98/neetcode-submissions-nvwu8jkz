class Node:
    def __init__(self, val: int=0, next: 'Node'=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)    # dummy head
        self.tail = self.head
        self.length = 0
    
    def get(self, index: int) -> int:
        if index > self.length:
            return -1

        curr = self.head.next
        while index:
            curr = curr.next
            index -= 1
        return curr.val

    def insertHead(self, val: int) -> None:
        node = Node(val, self.head.next)
        self.head.next = node
        if node.next == None:
            self.tail = node
        self.length += 1

    def insertTail(self, val: int) -> None:
        if self.length == 0:
            return self.insertHead(val)
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.length += 1

    def remove(self, index: int) -> bool:
        if index > self.length:
            return False

        curr = self.head
        while index:
            curr = curr.next
            index -= 1
        if curr.next == self.tail:
            self.tail = curr
        curr.next = curr.next.next
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        res = []

        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next

        return res
