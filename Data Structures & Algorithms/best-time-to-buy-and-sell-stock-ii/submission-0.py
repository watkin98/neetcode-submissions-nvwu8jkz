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
        buying = 0
        selling = 1
        for j in range(i+1, len(prices)):
            if selling:
                if prices[j] > prices[i]:
                    profit += prices[j]
                    i = j
                selling = 0
                buying = 1
            if buying:
                ####

                buying = 0
                selling = 1

        print(f"Profit: {profit}")