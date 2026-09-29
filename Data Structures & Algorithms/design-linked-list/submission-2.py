class Node:
    def __init__(self, val: int=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)       # Dummy node
        self.tail = self.head
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        print(1)
        curr = self.head.next
        while True:
            if not index:
                return curr.val
            curr = curr.next
            index -= 1

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head.next, self.head)
        self.head.next = node

        if node.next:
            node.next.prev = node

        if self.tail == self.head:
            self.tail = node
        
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.tail == self.head:
            return self.addAtHead(val)

        node = Node(val, None, self.tail)
        self.tail.next = node
        self.tail = node

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        if index == self.length:
            return self.addAtTail(val)
        if index == 0:
            return self.addAtHead(val)
        
        curr = self.head.next
        while index:
            curr = curr.next
            index -= 1

        node = Node(val, curr, curr.prev)
        curr.prev.next = node
        curr.prev = node

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return

        curr = self.head.next
        while index:
            curr = curr.next
            index -= 1

        curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)