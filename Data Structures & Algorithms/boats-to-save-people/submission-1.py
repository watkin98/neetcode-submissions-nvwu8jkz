class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        l, r = 0, len(people) - 1
        boats_needed = 0

        while l < r and people[l] == limit:
            boats_needed += 1
            people[l] = -1
            l += 1
        while r > l and people[r] == limit:
            boats_needed += 1
            people[r] = -1
            r -= 1

        while l < r:
            total = people[l] + people[r]
            if total > limit:
                r -= 1
            else:
                boats_needed += 1
                people[l] = -1
                people[r] = -1
                l += 1
                r -= 1
        print(boats_needed)
        print(people)
        for i in range(len(people)):
            if people[i] != -1:
                boats_needed += 1

        return boats_needed

