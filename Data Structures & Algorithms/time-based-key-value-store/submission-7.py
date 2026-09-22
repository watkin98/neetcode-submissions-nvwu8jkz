class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        timestamps = self.hashmap[key]

        l, r = 0, len(timestamps) - 1
        res = ""

        while l <= r:
            m = l + ((r-l) // 2)

            time = timestamps[m]

            if time[0] <= timestamp:
                res = time[1]
                l = m + 1
            else:
                r = m - 1
        return res