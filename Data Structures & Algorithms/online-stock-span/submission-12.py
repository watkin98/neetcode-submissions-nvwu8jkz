class StockSpanner:

    def __init__(self):
        self.stocks = []     # (price, span) pairs

    def next(self, price: int) -> int:
        span = 1
        while self.stocks and self.stocks[-1][0] <= price:
            p, s = self.stocks.pop()
            span += s
        self.stocks.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)