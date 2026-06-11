class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        onesCount = 0

        for num in nums:
            if num == 1:
                onesCount += 1
                res = max(res, onesCount)
            else:
                onesCount = 0

        return res