class FreqStack:

    def __init__(self):
        self.stacks = defaultdict(list)
        self.highestFreq = 0
        self.frequencies = defaultdict(int)

    def push(self, val: int) -> None:
        self.frequencies[val] += 1
        valFreq = self.frequencies[val]
        self.highestFreq = max(self.highestFreq, valFreq)
        self.stacks[valFreq].append(val)

    def pop(self) -> int:
        res = self.stacks[self.highestFreq].pop()
        self.frequencies[res] -= 1

        if self.stacks[self.highestFreq] == []:
            self.highestFreq -= 1
        
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()