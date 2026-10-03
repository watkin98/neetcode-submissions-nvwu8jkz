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
        #self.printNodes()
        res = self.hashmap[key].val if key in self.hashmap else -1
        if res != -1:
            self.updateCache(key)
        #self.printNodes()
        return res

    def put(self, key: int, value: int) -> None:
        #self.printNodes()
        if key in self.hashmap:
            self.hashmap[key].val = value
            self.updateCache(key)
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
        #self.printNodes()

    def removeLRU(self) -> None:
        temp = self.cacheTail.prev
        self.cacheTail.prev.next = None
        #print(self.hashmap.items())
        del self.hashmap[self.cacheTail.key]
        #print(self.hashmap.items())
        self.cacheTail = temp
        self.count -= 1

    def updateCache(self, key: int) -> None:
        node = self.hashmap[key]
        if self.cacheHead.next == node:
            return
        node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev
        else:
            self.cacheTail = node.prev
        
        if self.cacheHead.next != None:
            self.cacheHead.next.prev = node
        node.next = self.cacheHead.next
        node.prev = self.cacheHead
        self.cacheHead.next = node

    def printNodes(self) -> None:
        curr = self.cacheHead.next

        while curr:
            print(curr.val)
            curr = curr.next
        print()

        
