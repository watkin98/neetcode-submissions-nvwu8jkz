class Node:
    def __init__(self, val: int=0, key: int=None, next: Node=None, prev: Node=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cacheHead = Node(-1)   # dummy head of a linked list
        self.cacheTail = self.cacheHead
        self.hashmap = defaultdict(int)

    def get(self, key: int) -> int:
        return self.hashmap[key].val if key in self.hashmap else -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].val = value
            return

        node = Node(value, key, self.cacheHead.next, self.cacheHead)
        if self.cacheTail == self.cacheHead:
            self.cacheTail = node
        else:
            self.cacheHead.next.prev = node
        self.cacheHead.next = node
        
        self.count += 1
        self.hashmap[key] = node

        if self.count > self.capacity:
            self.removeLRU()

    def removeLRU(self) -> None:
        temp = self.cacheTail.prev
        self.cacheTail.prev.next = None
        del self.hashmap[self.cacheTail.key]
        self.cacheTail = temp
        self.count -= 1
        
