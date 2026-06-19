class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [0] * len(nums)
        resIndex = len(nums) - 1

        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                res[resIndex] = nums[l] * nums[l]
                l += 1
            else:
                res[resIndex] = nums[r] * nums[r]
                r -= 1

            resIndex -= 1

        return res