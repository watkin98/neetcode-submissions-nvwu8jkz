class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        cars.sort(reverse=True)
        fleets = []

        for car in cars:
            time = (target - car[0]) / car[1]
            if not fleets or fleets[-1] < time:
                fleets.append(time)

        return len(fleets)