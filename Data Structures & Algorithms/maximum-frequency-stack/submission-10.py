class FreqStack:

    def __init__(self):
        self.stacks = {}
        self.freqs = {}
        self.most_frq = 0

    def push(self, val: int) -> None:
        val_freq = 1 + self.freqs.get(val, 0)
        self.freqs[val] = val_freq
        if val_freq not in self.stacks:
            self.stacks[val_freq] = [val]
        else:
            freq_stack = self.stacks.get(val_freq)
            freq_stack.append(val)
        self.most_frq = max(self.most_frq, val_freq)

    def pop(self) -> int:
        res = self.stacks[self.most_frq].pop()
        if not self.stacks[self.most_frq]:
            while True:
                self.most_frq -= 1
                if self.stacks[self.most_frq] or not self.most_frq:
                    break

        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()