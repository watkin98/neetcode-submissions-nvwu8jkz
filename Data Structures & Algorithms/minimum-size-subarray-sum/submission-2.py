class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curSum = 0
        l = 0
        res = len(nums) + 1

        for r in range(len(nums)):
            curSum += nums[r]

            if curSum >= target:
                res = min(res, r - l + 1)

            while l < r and curSum >= target:
                curSum -= nums[l]
                l += 1

                if curSum >= target:
                    res = min(res, r - l + 1)

        return res if res != len(nums) + 1 else 0