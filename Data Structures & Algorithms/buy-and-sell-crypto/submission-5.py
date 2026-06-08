class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]

            if profit < 0:
                l += 1
                #r += 1
            elif profit > maxProfit:
                maxProfit = profit
                r += 1
            else:
                r += 1

        return maxProfit