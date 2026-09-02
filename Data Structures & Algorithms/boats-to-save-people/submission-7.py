class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l, r = 0, len(people) - 1
        while r > 0 and people[r] == limit:
            res += 1
            r -= 1

        while l < r:
            if people[l] + people[r] > limit:
                res += 1
                r -= 1
            else:      # people[l] + people[r] <= limit:
                res += 1
                r -= 1
                l += 1

        return res if l != r else res + 1