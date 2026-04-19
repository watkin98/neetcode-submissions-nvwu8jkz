class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0
        lcs = 0
        res = 0
        if nums == []:
            return 0
        lowest = nums[0]
        keys = {}

        for num in nums:
            if num < lowest:
                lowest = num
            keys[num] = None

        counter = lowest
        while counter <= 1000 and counter <= len(nums):
            if counter in nums:
                lcs += 1
                counter += 1
                continue
            
            if lcs > res:
                res = lcs
            
            lcs = 0
            counter += 1

        if lcs > res:
            res = lcs

        return res