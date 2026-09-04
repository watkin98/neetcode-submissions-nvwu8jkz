class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = min(piles), max(piles)
        k = r

        while l <= r:
            rate = l + ((r-l) // 2)
            time = 0
            piles_copy = piles.copy()
            count = 0
            while count < len(piles_copy):
                piles_copy[count] -= rate
                if piles_copy[count] <= 0:
                    count += 1
                time += 1
            
            if time <= h:
                k = min(k, rate)
                r = rate - 1
            else:
                l = rate + 1
    
        return k
