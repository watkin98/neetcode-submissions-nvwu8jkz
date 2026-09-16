class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        counter = 0
        curr = self.head

        while curr != None and counter < index:
            curr = curr.next
            counter += 1

        return curr.val if counter == 0 else -1

    def insertHead(self, val: int) -> None:
        temp = self.head
        self.head = Node(val)
        self.head.next = temp   

    def insertTail(self, val: int) -> None:
        curr = self.head
        while curr.next != None:
            curr = curr.next

        curr.next = Node(val)

    def remove(self, index: int) -> bool:
        counter = 0
        curr = self.head
        prev = None

        while curr != None and counter < index:
            prev = curr
            curr = curr.next
            counter += 1

        if counter == index:
            prev.next = curr.next
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        nums = []
        curr = self.head

        while curr != None:
            nums.append(curr.val)
            curr = curr.next
        
        return nums