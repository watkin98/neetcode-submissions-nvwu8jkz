class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        candidate = None

        while l <= r:
            capacity = l + ((r-l) // 2)
 
            time = load = 0
            for w in weights:
                load += w
                if load > capacity:
                    load = w
                    time += 1
            time += 1
            print(time)
            if time > days:
                l = capacity + 1
            elif time <= days:
                candidate = capacity
                r = capacity - 1

        return candidate