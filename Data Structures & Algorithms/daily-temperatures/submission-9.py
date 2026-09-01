class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []      # pair: (temp, index)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                top_temp, top_i = stack.pop()
                res[top_i] = i - top_i
            stack.append((temp, i))

        return res