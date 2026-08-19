class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people) - 1
        res = 0

        while l < r:
            weight = people[l] + people[r]

            if weight > limit:
                res += 1
                r -= 1
            else: 
                res += 1
                r -= 1
                l += 1

        return res if l != r else res + 1