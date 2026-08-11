class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        l, r = 0, len(people) - 1
        boats_needed = 0

        while people[l] == limit:
            boats_needed += 1
            l += 1
        while people[r] == limit:
            boats_needed += 1
            r -= 1

        while l < r:
            total = people[l] + people[r]
            if total > limit:
                r -= 1
            else:
                boats_needed += 1
                l += 1
                r -= 1

        return boats_needed if l != r else boats_needed + 1

