class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        n = len(position)

        for i in range(n):
            time_i = (target - position[i]) / speed[i]
            stack.append(time_i)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)