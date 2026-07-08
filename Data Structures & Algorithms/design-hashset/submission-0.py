class MyHashSet:

    def __init__(self):
        self.lst = []

    def add(self, key: int) -> None:
        for i in range(len(self.lst)):
            if self.lst[i] == key:
                return
        self.lst.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.lst)):
            if self.lst[i] == key:
                self.lst.remove(key)
                break

    def contains(self, key: int) -> bool:
        for i in range(len(self.lst)):
            if self.lst[i] == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)