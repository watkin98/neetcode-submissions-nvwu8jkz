class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars_sorted = list(zip(position, speed))
        cars_sorted.sort(reverse=True)
        n = len(position)

        for i in range(n):
            time = (target - cars_sorted[i][0]) / cars_sorted[i][1]
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)

        return len(stack)