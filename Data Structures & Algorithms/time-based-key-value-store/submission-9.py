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
            m = (l + r + 1) // 2

            if person[m][0] <= timestamp:
                l = m
            else:
                r = m - 1

        return person[l][1] if person[l][0] <= timestamp else ""
