class FreqStack:

    def __init__(self):
        self.stack = defaultdict(list)
        self.highest = 0
        self.freqs = defaultdict(int)

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        if self.freqs[val] > self.highest:
            self.highest = self.freqs[val]
        
        self.stack[self.freqs[val]].append(val)

    def pop(self) -> int:
        res = self.stack[self.highest].pop()
        self.freqs[res] -= 1

        while self.highest > 0 and self.stack[self.highest] == []:
            self.highest -= 1

        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()