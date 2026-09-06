class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot and call binary search on left and right portions (pivot == min(nums) index)
        l, r = 0, len(nums) - 1
        pivot = 0

        while l <= r:
            if nums[l] <= nums[r] and nums[pivot] > nums[l]:
                pivot = l
                break

            m = l + ((r-l) // 2)
            if nums[m] < nums[pivot]:
                pivot = m

            if nums[l] <= nums[m]:
                if nums[l] < nums[pivot]:
                    pivot = l
                l = m + 1
            else:
                r = m - 1
        left = self.binarySearch(nums, 0, m+1, target)
        right = self.binarySearch(nums, m+1, len(nums) - 1, target)
        
        if left != -1:
            return left
        elif right != -1:
            return right
        else:
            return -1


        
    def binarySearch(self, nums, l, r, target) -> int:
        while l <= r:
            m = l + ((r-l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1