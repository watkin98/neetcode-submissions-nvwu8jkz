class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            cap = l + ((r-l) // 2)

            time = i = 0
            temp_cap = cap
            while i < len(weights):
                while i < len(weights) and temp_cap - weights[i] >= 0:
                    temp_cap -= weights[i]
                    i += 1
                time += 1
                temp_cap = cap
                
            print(f"time: {time}\ncap: {cap}\n")

            if time > days:
                l = cap + 1
            else:
                res = cap
                r = cap - 1

        return res