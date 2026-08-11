class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroid_stack = []

        for asteroid in asteroids:
            if asteroid_stack == []:
                asteroid_stack.append(asteroid)
                continue
            
            if (asteroid_stack[-1] > 0 and asteroid < 0) or (asteroid_stack[-1] < 0 and asteroid > 0):
                fallout = max(abs(asteroid_stack.pop()), abs(asteroid))
                if fallout != abs(asteroid):  
                    asteroid_stack.append(fallout)
            else:
                asteroid_stack.append(asteroid)

        return asteroid_stack