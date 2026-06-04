class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highestProfit = 0
        
        for i, price1 in enumerate(prices):
            for j, price2 in enumerate(prices[i+1:]):
                # if i == j:
                #     continue

                if price2 - price1 > highestProfit:
                    highestProfit = price2 - price1

        return highestProfit