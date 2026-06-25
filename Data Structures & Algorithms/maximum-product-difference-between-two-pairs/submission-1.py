class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        minVals = [10001, 10001]
        maxVals = [-1, -1]

        for num in nums:
            if num < minVals[1]:
                minVals.append(num)
                minVals.sort()
                minVals.pop(2)
            if num > maxVals[0]:
                maxVals.append(num)
                maxVals.sort()
                maxVals.pop(0)

        return (maxVals[0] * maxVals[1]) - (minVals[0] * minVals[1])