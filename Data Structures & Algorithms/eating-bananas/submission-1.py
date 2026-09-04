class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1

        while True:
            time = 0

            for pile in piles:
                while pile > 0:
                    pile -= speed
                    time += 1

            if time <= h:
                return speed

            speed += 1
            
