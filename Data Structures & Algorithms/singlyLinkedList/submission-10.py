class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)        # Dummy node for head
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next

        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        if self.tail == self.head:
            self.tail = node
        self.head.next = node

    def insertTail(self, val: int) -> None:
        node = Node(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        while curr and curr.next:
            if i == index:
                curr.next = curr.next.next
                if curr.next == None:
                    self.tail = curr
                return True
            curr = curr.next
            i += 1
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next

        while curr:
            res.append(curr.val)
            curr = curr.next

        return res

