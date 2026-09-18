class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        curr = self.head.next
        i = 0

        while i < index:
            curr = curr.next
            i += 1
        return curr.val


    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head.next)
        if self.head.next == None:
            self.tail = node
        self.head.next = node
        self.length += 1


    def addAtTail(self, val: int) -> None:
        if self.tail == self.head:
            self.addAtHead(val)

        node = Node(val, None, self.tail)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        if index == self.length:
            self.addAtTail(val)
            return

        i = 0
        curr = self.head.next
        while i < index:
            curr = curr.next
            i += 1
        node = Node(val, curr, curr.prev)
        curr.prev.next = node
        curr.prev = node
        self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index > self.length:
            return
        elif index == 0:
            self.head.next = self.head.next.next
            self.head.next.prev = None
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            i = 0
            curr = self.head.next

            while i < index:
                curr = curr.next
                i += 1
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