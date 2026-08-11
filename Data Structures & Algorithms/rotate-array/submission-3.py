class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L, R = 0, k

        while R < len(nums):
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R += 1