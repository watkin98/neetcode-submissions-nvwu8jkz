class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = {}

        for i in range(len(position)):
            pairs[position[i]] = speed[i]

        pairs = list(pairs.items())
        pairs.sort(reverse=True)
        
        for pos, spd in pairs:
            stack.append((target - pos) / spd)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        
