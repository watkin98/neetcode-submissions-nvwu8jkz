class MyHashSet:

    def __init__(self):
        self.hashset = [0] * 1000

    def add(self, key: int) -> None:
        index = key % 999
        if self.hashset[index]:
            return
        self.hashset[index] = key

    def remove(self, key: int) -> None:
        index = key % 999
        if self.hashset[index]:
            self.hashset[index] = 0

    def contains(self, key: int) -> bool:
        return self.hashset[key % 999] != 0


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)