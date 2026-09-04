class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        #l, r = 0, len(piles) - 1
        res = piles[-1]

        for i in range(len(piles)):
            time = 0

            for pile in piles:
                while pile > 0:
                    pile -= piles[i]
                    time += 1

            if time <= h:
                res = min(res, piles[i])

        return res
