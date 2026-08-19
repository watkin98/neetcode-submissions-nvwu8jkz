class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        self.stocks.append(price)
        res = 0
        stock_check = []

        for stock in self.stocks:
            stock_check.append(stock)

        while stock_check and stock_check[-1] <= price:
            stock_check.pop()
            res += 1

        return res




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)