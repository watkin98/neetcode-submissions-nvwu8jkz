class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroid_stack = []

        for asteroid in asteroids:
            if asteroid_stack == []:
                asteroid_stack.append(asteroid)
                continue
            
            if (asteroid_stack[-1] > 0 and asteroid < 0):
                left, right = asteroid_stack[-1], asteroid
                if abs(left) > abs(right):
                    continue
                elif abs(left) < abs(right):
                    asteroid_stack.pop()
                    asteroid_stack.append(asteroid)
                else:
                    asteroid_stack.pop()
            else:
                asteroid_stack.append(asteroid)

        return asteroid_stack