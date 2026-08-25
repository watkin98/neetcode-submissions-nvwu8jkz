class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                collision = stack[-1] + a

                if collision > 0:
                    a = 0
                elif collision < 0:
                    stack.pop()
                else:
                    a = 0
                    stack.pop()

            if a:
                stack.append(a)

        return stack