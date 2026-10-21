class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        
        times = []
        for p, s in cars:
            time = (target - p) / s
            if not times or time > times[-1]:
                times.append(time)
        return len(times)