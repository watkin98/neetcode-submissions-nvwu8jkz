class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = float('inf')
        while l <= r:
            capacity = l + ((r-l) // 2)
            load = time = 0

            for w in weights:
                load += w

                if load > capacity:
                    load = w
                    time += 1
            time += 1

            if time <= days:
                res = capacity
                r = capacity - 1
            else:
                l = capacity + 1

        return res