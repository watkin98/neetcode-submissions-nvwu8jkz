class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r

        while l <= r:
            rate = l + ((r-l) // 2)
            time = 0

            for p in piles:
                time += (p // rate) + 1 if (p % rate) > 0 else (p // rate)
            
            if time <= h:
                k = min(k, rate)
                r = rate - 1
            else:
                l = rate + 1
    
        return k
