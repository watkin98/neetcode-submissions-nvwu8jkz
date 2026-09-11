class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        res = ""
        for item in self.hashmap[key]:
            if item[1] <= timestamp:
                res = item[0]

        return res
