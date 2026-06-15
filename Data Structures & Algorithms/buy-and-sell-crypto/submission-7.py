class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0

        for i in range(len(prices)):
            for j in range(len(prices)):
                if i >= j:
                    continue

                maxProf = max(maxProf, prices[j] - prices[i])

        return maxProf