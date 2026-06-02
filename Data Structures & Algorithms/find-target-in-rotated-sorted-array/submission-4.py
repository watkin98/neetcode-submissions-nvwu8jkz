class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] == target:
                    return l

            if nums[r] == target:
                    return r

            mid = l + (r - l) // 2
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                if target > nums[l]:
                    r = mid - 1
                else:
                    l += 1
            else:
                if target < nums[r]:
                    l = mid + 1
                else:
                    r -= 1
                

        return -1