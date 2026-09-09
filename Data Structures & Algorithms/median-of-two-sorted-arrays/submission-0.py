class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()

        return float(nums[(len(nums) - 1) // 2]) if len(nums) % 2 == 1 else float((nums[(len(nums) - 1) // 2] + nums[((len(nums) - 1) // 2) + 1]) / 2)