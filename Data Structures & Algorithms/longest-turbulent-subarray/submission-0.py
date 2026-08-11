class Solution:
    def maxTurbulenceSize(self, nums: List[int]) -> int:
        res = 1
        i = 0

        while i < len(nums) - 1 and nums[i] == nums[i+1]:
            i += 1

        if i == len(nums) - 1:
            return res
        
        increasing = False
        curMax = 1
        if nums[i+1] > nums[i]:
            increasing = True

        i += 1
        curMax += 1
        res += 1

        for i in range(i, len(nums) - 1):
            if increasing and nums[i+1] > nums[i]:
                curmax = 1
            elif increasing and nums[i+1] < nums[i]:
                increasing = False
                curMax += 1
                res = max(res, curMax)
            elif not increasing and nums[i+1] > nums[i]:
                increasing = True
                curMax += 1
                res = max(res, curMax)
            elif not increasing and nums[i+1] < nums[i]:
                curMax = 1

        return res