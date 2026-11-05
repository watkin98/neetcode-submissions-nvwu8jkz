class FreqStack:

    def __init__(self):
        self.stacks = {}
        self.mst_frq = 0
        self.freqs = {}

    def push(self, val: int) -> None:
        if val not in self.freqs:
            self.freqs[val] = 0
        self.freqs[val] += 1

        val_freq = self.freqs[val]
        if val_freq not in self.stacks:
            self.stacks[val_freq] = []
        self.stacks[val_freq].append(val)

        self.mst_frq = max(self.mst_frq, val_freq)

    def pop(self) -> int:
        res = self.stacks[self.mst_frq].pop()
        print(self.stacks)
        print(self.mst_frq)
        print()
        while not self.stacks[self.mst_frq]:
            self.mst_frq -= 1
        self.freqs[res] -= 1

        return res
        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()