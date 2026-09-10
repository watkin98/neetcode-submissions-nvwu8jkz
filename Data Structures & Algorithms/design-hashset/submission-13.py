class MyHashSet:

    def __init__(self):
        self.hashset = [[-1] for _ in range(1001)]

    def add(self, key: int) -> None:
        index = key % 1000
        if self.hashset[index] != [-1] and key in self.hashset[index]:
            return
        self.hashset[index].append(key)

    def remove(self, key: int) -> None:
        index = key % 1000
        if self.hashset[index] != [-1] and key in self.hashset[index]:
            self.hashset[index].remove(key)

    def contains(self, key: int) -> bool:
        return False if self.hashset[key % 1000] == [-1] else key in self.hashset[key % 1000]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)