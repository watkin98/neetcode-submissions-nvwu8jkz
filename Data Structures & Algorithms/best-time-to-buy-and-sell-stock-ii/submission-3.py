class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i, price in enumerate(prices):
            if i < len(prices) - 1 and prices[i+1] <= price:
                continue
            
            if i == len(prices) - 1:
                continue
            profit += prices[i+1] - price

        return profit
            