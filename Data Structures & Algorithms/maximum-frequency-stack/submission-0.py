class FreqStack:

    def __init__(self):
        self.stack = []
        self.freqMap = defaultdict(int)
        self.mostFreq = 0
        self.freqMap[0] = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freqMap[val] += 1

        for value in self.freqMap:
            if self.freqMap[value] > self.freqMap[self.mostFreq]:
                self.mostFreq = value
        
    def pop(self) -> int:
        tempStack = []
        tempSet = set()
        tempSet.add(self.mostFreq)

        for val in self.freqMap:
            if self.freqMap[val] == self.freqMap[self.mostFreq]:
                tempSet.add(val)

        while self.stack[-1] not in tempSet:
            tempStack.append(self.stack.pop())

        res = self.stack.pop()
        self.freqMap[res] -= 1

        while tempStack:
            self.stack.append(tempStack.pop())

        for value in self.freqMap:
            if self.freqMap[value] > self.freqMap[self.mostFreq]:
                self.mostFreq = value

        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()