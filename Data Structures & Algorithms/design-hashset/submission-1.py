class MyHashSet:

    def __init__(self):
        self.hashSet = [0] * 1000000

    def add(self, key: int) -> None:
        self.hashSet[key] += (1 if self.hashSet[key] == 0 else 0)

    def remove(self, key: int) -> None:
        self.hashSet[key] -= (1 if self.hashSet[key] else 0)

    def contains(self, key: int) -> bool:
        return True if self.hashSet[key] > 0 else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)