class Node:

    def __init__(self, val: int=0, nxt: Node=None, prev: Node=None):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1, None, self.head)
        self.head.next = self.tail
        self.length = 0

    def get(self, index: int) -> int:
        if index > self.length:
            return -1

        curr = self.head.next
        while index:
            curr = curr.next
            index -= 1
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head.next, self.head)
        self.head.next.prev = node
        self.head.next = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val, self.tail, self.tail.prev)
        self.tail.prev.next = node
        self.tail.prev = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        if index == self.length:
            node = Node(val, self.tail, self.tail.prev)
            self.tail.prev.next = node
            self.length += 1
            self.tail.prev = node
            return

        curr = self.head.next
        while index:
            curr = curr.next
            index -= 1
        node = Node(val, curr, curr.prev)
        curr.prev.next = node
        curr.prev = node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        print(1)
        print(index)
        print(self.length)
        print()
        if index >= self.length:
            return

        curr = self.head.next
        while index:
            curr = curr.next
            index -= 1
        
        curr.prev.next = curr.next 
        curr.next.prev = curr.prev
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)