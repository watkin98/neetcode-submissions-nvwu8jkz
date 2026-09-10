class MyHashSet:

    def __init__(self):
        self.hashset = [-1] * 1001

    def add(self, key: int) -> None:
        index = key % 1000
        if self.hashset[index] != -1:
            return
        self.hashset[index] = key

    def remove(self, key: int) -> None:
        index = key % 1000
        if self.hashset[index] != -1:
            self.hashset[index] = -1

    def contains(self, key: int) -> bool:
        return self.hashset[key % 1000] != -1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)