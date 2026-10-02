class Node:
    def __init__(self, val: int=0, next: Node=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)    # dummy head node
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next

        while curr:
            if index == 0:
                return curr.val
            index -= 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val, self.head.next)
        if self.tail == self.head:
            self.tail = node
        self.head.next = node

    def insertTail(self, val: int) -> None:
        if self.tail == self.head:
            return self.insertHead(val)
        
        node = Node(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        if not self.head.next:
            return False
            
        curr = self.head

        while curr:
            if index == 0:
                if self.tail == curr.next:
                    self.tail = curr
                curr.next = curr.next.next if curr.next else None
                return True
            index -= 1
            curr = curr.next

        return False


    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next

        while curr:
            res.append(curr.val)
            curr = curr.next

        return res

