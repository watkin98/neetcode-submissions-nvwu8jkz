class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float('inf')
        curSum = 0

        for r in range(len(nums)):
            curSum += nums[r]
            if curSum >= target:
                res = min(res, r-l+1)

            while l < r and curSum - nums[l] >= target:
                curSum -= nums[l]
                l += 1
                res = min(res, r-l+1)

        return res if res != float('inf') else 0
            