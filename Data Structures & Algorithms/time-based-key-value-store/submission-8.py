class TimeMap:

    def __init__(self):
        self.persons = defaultdict(list)    # key-tuple pairs

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.persons[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.persons:
            return ""

        person = self.persons[key]

        l, r = 0, len(person) - 1
        while l < r:
            m = l + ((r-l) // 2)

            if person[m][0] < timestamp:
                l = m + 1
            else:
                r = m

        return person[l][1]
