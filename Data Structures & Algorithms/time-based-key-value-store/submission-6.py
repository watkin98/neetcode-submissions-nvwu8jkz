class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        items = self.hashmap[key]
        l, r = 0, len(items) - 1
        res = ""
        while l <= r:
            m = l + ((r-l) // 2)
            value, item_timestamp = items[m]

            if item_timestamp < timestamp:
                res = value
                l = m + 1
            elif item_timestamp > timestamp:
                r = m - 1
            else:
                return value

        return res
