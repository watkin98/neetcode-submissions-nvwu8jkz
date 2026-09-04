class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            curTemp = temperatures[i]
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > curTemp:
                    res.append(j-i)
                    break
            if len(res) != i + 1:
                res.append(0)

        return res