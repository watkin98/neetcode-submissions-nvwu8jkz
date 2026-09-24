class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            candidate = l + ((r-l) // 2)

            load = time = 0
            for w in weights:
                load += w

                if load > candidate:
                    load = w
                    time += 1
            time += 1

            if time <= days:
                res = candidate
                r = candidate - 1
            else:
                l = candidate + 1
        return res