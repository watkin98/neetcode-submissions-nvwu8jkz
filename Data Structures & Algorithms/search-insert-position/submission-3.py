class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r, res = 0, len(nums)-1, len(nums)

        while l <= r:
            mid = l + (r - l) // 2

            if target > nums[mid]:
                res = mid
                r = mid - 1 
            elif target < nums[mid]:
                l = mid + 1
            else:
                return mid
            
        return res