class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                lower_day = stack.pop()
                res[lower_day[1]] = i - lower_day[1]
            stack.append([temperatures[i], i])
        return res

