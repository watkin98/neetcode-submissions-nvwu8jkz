class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(list(zip(position, speed)), reverse=True)
        fleets = []

        for p in pairs:
            time = (target - p[0]) / p[1]
            
            if not fleets or fleets[-1] < time:
                fleets.append(time)

        return len(fleets)
