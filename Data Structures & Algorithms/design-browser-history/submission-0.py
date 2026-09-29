class BrowserHistory:

    def __init__(self, homepage: str):
        self.s1 = []
        self.s2 = []

        self.s1.append(homepage)

    def visit(self, url: str) -> None:
        self.s1.append(url)
        self.s2 = []
        #print(self.s1)

    def back(self, steps: int) -> str:
        while len(self.s1) > 1 and steps:
            self.s2.append(self.s1.pop())
            steps -= 1
        #self.s1.append(self.s2.pop())
        #print(self.s1)
        #print(self.s1[-1])
        return self.s1[-1]

    def forward(self, steps: int) -> str:
        while len(self.s2) > 1 and steps:
            self.s1.append(self.s2.pop())
            steps -= 1
        
        return self.s1[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)