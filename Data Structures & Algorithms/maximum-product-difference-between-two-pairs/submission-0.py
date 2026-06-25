class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) - 1
        return (nums[n] * nums[n - 1]) - (nums[0] * nums[1])