class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find first day to buy
        bought = False
        i = 0

        while bought is False and i < len(prices) - 1:
            if prices[i+1] <= prices[i]:
                i += 1
                continue
            bought = True

        #print(f"Buy in: {profit}")
        # begin trading
        profit = 0
        buying = 0
        selling = 1
        hold = 0
        for j in range(i+1, len(prices)):
            if selling and prices[j] > prices[i]:
                transaction = prices[j] - prices[i]
                profit += transaction
                i = j
                selling = 0
                buying = 1
            if buying and prices[j] < prices[i]:
                ####
                i = j
                buying = 0
                selling = 1

        profit = max(profit, prices[len(prices)-1] - prices[i-1])
        return profit