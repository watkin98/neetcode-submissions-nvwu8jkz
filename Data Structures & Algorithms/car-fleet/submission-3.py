class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack_pos = []
        stack = []
        n = len(position)
        
        for i in range(n):
            stack_pos.append([position[i], speed[i]])

        stack_pos.sort()

        for i in range(n):
            car = stack_pos.pop()
            time_i = (target - car[0]) / car[1]
            stack.append(time_i)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)