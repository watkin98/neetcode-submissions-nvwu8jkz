class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []      # (temp, i) pairs

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                old_temp, index = stack.pop()
                res[index] = i - index
            stack.append((temp, i))

        return res
