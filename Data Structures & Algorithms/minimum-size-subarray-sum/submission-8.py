class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        total = 0

        l = 0
        for r in range(len(nums)):
            total += nums[r]

            if total >= target:
                res = min(res, r-l+1)
            while total >= target:
                total -= nums[l]
                l += 1
                
                if total >= target:
                    res = min(res, r-l+1)

        return res if res != float('inf') else 0