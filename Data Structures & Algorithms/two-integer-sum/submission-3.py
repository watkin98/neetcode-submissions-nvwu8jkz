class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}

        for i, num in enumerate(nums):
            difference = target - num
            print(difference)
            print(numHash.items())
            if difference in numHash:
                return [numHash[difference], i]
            else:
                numHash[num] = i

        return [-1, -1]