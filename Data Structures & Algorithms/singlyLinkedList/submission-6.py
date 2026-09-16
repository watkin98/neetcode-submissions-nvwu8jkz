class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        counter = 0
        curr = self.head.next

        while curr and counter < index:
            curr = curr.next
            counter += 1

        return curr.val if curr and counter == index else -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val, self.head.next)
        self.head.next = newNode
        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        counter = 0
        curr = self.head

        while curr.next and counter < index:
            curr = curr.next
            counter += 1

        if curr.next and counter == index:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        nums = []
        curr = self.head.next

        while curr:
            nums.append(curr.val)
            curr = curr.next

        return nums
