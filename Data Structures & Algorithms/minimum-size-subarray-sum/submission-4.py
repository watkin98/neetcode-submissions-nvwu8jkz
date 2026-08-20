class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curSum = nums[0]
        res = len(nums) + 1 if nums[0] < target else 1

        for r in range(1, len(nums)):
            curSum += nums[r]

            if curSum < target:
                continue
            else:
                res = min(res, r - l + 1)

                while curSum - nums[l] >= target:
                    curSum -= nums[l]
                    l += 1
                    res = min(res, r - l + 1)

        return res if res != len(nums) + 1 else 0