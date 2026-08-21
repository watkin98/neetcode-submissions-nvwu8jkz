class FreqStack:

    def __init__(self):
        self.counts = defaultdict(int)
        self.stacks = defaultdict(list)
        self.maxCnt = 0

    def push(self, val: int) -> None:
        self.counts[val] += 1
        self.maxCnt = max(self.maxCnt, self.counts[val])
        self.stacks[self.counts[val]].append(val)
        

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.counts[res] -= 1
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()