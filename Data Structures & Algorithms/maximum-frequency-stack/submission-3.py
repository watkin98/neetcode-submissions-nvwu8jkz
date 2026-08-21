class FreqStack:

    def __init__(self):
        self.stack = []
        self.stack_tracker = defaultdict(int)
        self.max_instances = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stack_tracker[val] += 1

        self.max_instances = max(self.max_instances, self.stack_tracker[val])

    def pop(self) -> int:
        max_freqs = set()
        for val in self.stack_tracker:
            if self.stack_tracker[val] == self.max_instances:
                max_freqs.add(val)

        res = None
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] in max_freqs:
                res = self.stack[i]
                del self.stack[i]
                self.stack_tracker[res] -= 1
                break
        self.max_instances = 0
        for val in self.stack_tracker:
            self.max_instances = max(self.max_instances, self.stack_tracker[val])
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()