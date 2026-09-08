class MyCircularQueue:
    class Node:
        def __init__(self, val=None):
            self.value = val
            self.next = None

    def __init__(self, k: int):
        self.capacity = k
        self.length = 0
        self.head = self.Node()
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.length == self.capacity:
            return False
        
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = self.tail = self.Node(value)
        
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.length == 0:
            return False

        self.head = self.head.next
        self.length -= 1
        return True

    def Front(self) -> int:
        if self.length == 0:
            return -1
        return self.head.next.value

    def Rear(self) -> int:
        if self.length == 0:
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()