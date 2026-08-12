class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        i = len(self.stack) - 1

        while i >= 0:
            if self.stack[i] <= price:
                count += 1
                i -= 1
            else:
                break
        self.stack.append(price)

        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)