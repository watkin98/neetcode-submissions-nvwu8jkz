class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newNums = [0] * (n * 2)

        for i in range(n):
            newNums[i] = nums[i]
            newNums[i + n] = nums[i]

        return newNums