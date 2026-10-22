class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.pointers = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, val):
        node = Node(val, self.tail, self.tail.prev)

        self.tail.prev.next = node
        self.tail.prev = node

        self.pointers[val] = node

    def delete(self, val):
        node = self.pointers[val]
        node.prev.next = node.next
        node.next.prev = node.prev

    def top(self):
        return self.head.next.val

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.freqs = {}
        self.queue = LinkedList()

        for num in nums:
            if num not in self.freqs:
                self.freqs[num] = True
                self.queue.append(num)
            elif self.freqs[num] == True:
                self.freqs[num] = False
                self.queue.delete(num)
            else:
                continue

        # print(self.freqs)
        # curr = self.queue.head.next
        # res = []
        # while curr.val != -1:
        #     res.append(curr.val)
        #     curr = curr.next
        # print(res)

    def showFirstUnique(self) -> int:
        return self.queue.top()

    def add(self, value: int) -> None:
        if value not in self.freqs:
            self.freqs[value] = True
            self.queue.append(value)
        elif self.freqs[value] == True:
            self.freqs[value] = False
            self.queue.delete(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
