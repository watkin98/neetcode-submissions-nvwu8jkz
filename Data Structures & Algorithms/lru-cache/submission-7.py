class LinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1, None, self.head)
        self.head.next = self.tail
        self.length = 0

    def insertAtHead(self, node: 'Node'):
        if node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

        temp = self.head.next
        if node == self.tail.prev:
            self.tail.prev = self.tail.prev.prev

        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head
        

    def removeAtTail(self):
        if self.tail.prev == self.head:
            return None

        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        return node.key


class Node:

    def __init__(self, val: int=0, next: 'Node'=None, prev: 'Node'=None, key: int=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = LinkedList()
        self.keys = {}  # key-node pairs

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1

        node = self.keys[key]
        self.lru.insertAtHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            node.val = value
            self.lru.insertAtHead(node)
        else:
            node = Node(value, key=key)
            self.keys[key] = node
            self.lru.length += 1
            self.lru.insertAtHead(node)

        if self.lru.length > self.capacity:
            key_for_del = self.lru.removeAtTail()
            del self.keys[key_for_del]
            self.lru.length -= 1
