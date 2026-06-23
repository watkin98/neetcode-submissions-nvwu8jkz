class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                res.insert(0, nums[l] * nums[l])
                l += 1
            else:
                res.insert(0, nums[r] * nums[r])
                r -= 1
        
        return res