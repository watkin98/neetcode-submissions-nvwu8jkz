class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        negativeNumsSquared = []

        for num in nums:
            if num < 0:
                negativeNumsSquared.insert(0, (num * num))
            else:
                res.append(num * num)
        print(res)
        print(negativeNumsSquared)

        if res == []:
            return negativeNumsSquared

        for negNum in negativeNumsSquared:
            for i, resNum in enumerate(res):
                if negNum >= resNum and i + 1 < len(res) and negNum < res[i + 1]:
                    print('_______')
                    print(negNum)
                    print(resNum)
                    res.insert(i + 1, negNum)
                    break

        return res
