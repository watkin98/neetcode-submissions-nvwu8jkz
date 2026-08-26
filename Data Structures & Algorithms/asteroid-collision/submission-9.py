class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] > abs(a):
                    a = 0
                elif stack[-1] < abs(a):
                    stack.pop()
                else:
                    stack.pop()
                    a = 0
            if a:
                stack.append(a)
                
        return stack