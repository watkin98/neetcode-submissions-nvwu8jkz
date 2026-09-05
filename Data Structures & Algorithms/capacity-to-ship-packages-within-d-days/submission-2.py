class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = None

        while l <= r:
            cap = l + ((r-l) // 2)
            
            time = load = 0
            for w in weights:
                load += w

                if load > cap:
                    load = w
                    time += 1
            time += 1       # account for final load 

            if time > days:
                l = cap + 1
            else:
                res = cap
                r = cap - 1

        return res