class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        for item in self.hashset:
            if item == key:
                return

        self.hashset.append(key)

    def remove(self, key: int) -> None:
        self.hashset.remove(key) if self.contains(key) else None

    def contains(self, key: int) -> bool:
        for item in self.hashset:
            if item == key:
                return True

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)