class FreqStack:

    def __init__(self):
        self.frequencies = defaultdict(int)
        self.highest_freq = 0
        self.stacks = defaultdict(list)

    def push(self, val: int) -> None:
        self.frequencies[val] += 1
        self.highest_freq = max(self.highest_freq, self.frequencies[val])
        self.stacks[self.frequencies[val]].append(val)

    def pop(self) -> int:
        res = self.stacks[self.highest_freq].pop()
        self.frequencies[res] -= 1
        if self.stacks[self.highest_freq] == []:
            self.highest_freq -= 1

        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()