class MyHashSet:

    def __init__(self):
        self.hashset = [[] for i in range(1000)]

    def add(self, key: int) -> None:
        index = key % 1000
        if key not in self.hashset[index]:
            self.hashset[index].append(key)

    def remove(self, key: int) -> None:
        index = key % 1000
        if key in self.hashset[index]:
            self.hashset[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % 1000
        return True if key in self.hashset[index] else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)