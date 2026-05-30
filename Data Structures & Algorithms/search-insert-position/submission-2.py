class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r, res = 0, len(nums)-1, len(nums)

        while l <= r:
            mid = l + (r - l) // 2

            if target == nums[mid]:
                return mid
            elif nums[mid] > target:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res