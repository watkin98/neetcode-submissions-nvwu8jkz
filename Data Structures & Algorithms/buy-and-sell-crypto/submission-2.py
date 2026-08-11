class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = 0, 1, 0

        while sell < len(prices):
            transaction = prices[sell] - prices[buy]
            print(f"sell, buy, trans = {sell}, {buy}, {transaction}")
            if transaction > profit:
                profit = transaction
                sell += 1
                print(transaction)
            else:
                if transaction < 0:
                    buy += 1

                sell += 1
        
        return profit