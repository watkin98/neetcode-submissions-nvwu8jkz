class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        l = 0
        total = 0

        for r in range(len(nums)):
            total += nums[r]

            if total >= target:
                res = min(res, r-l+1)

                while l < r and total - nums[l] >= target:
                    total -= nums[l]
                    l += 1
                    res = min(res, r-l+1)

        return res if res != len(nums) + 1 else 0