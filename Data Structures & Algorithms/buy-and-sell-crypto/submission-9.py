class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowestBuy = prices[0]

        for price in prices:
            lowestBuy = min(lowestBuy, price)
            profit = max(profit, price - lowestBuy)

        return profit