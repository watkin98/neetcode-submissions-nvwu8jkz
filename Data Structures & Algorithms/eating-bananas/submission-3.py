class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = float("-inf")

        for pile in piles:
            maxPile = max(maxPile, pile)

        l, r = 1, maxPile
        res = r

        while l <= r:
            m = l + ((r-l) // 2)

            time = 0
            # for pile in piles:
            #     while pile > 0:
            #         pile -= m
            #         time += 1
            for p in piles:
                time += math.ceil(float(p) / m)

            if time > h:
                l = m + 1
            else:
                res = m
                r = m - 1
                #l += 1

        return res