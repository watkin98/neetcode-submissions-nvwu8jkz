class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pivot = self.findPivot(nums, target)
        print(f"Pivot {pivot}: {nums[pivot]}")
        return self.binarySearch(nums, 0, pivot-1, target) or self.binarySearch(nums, pivot, len(nums) - 1, target)

    def findPivot(self, nums, target) -> int:
        l, r = 0, len(nums) - 1
        pivot = nums[0]

        while l <= r:
            print(f"l, r: {l}, {r}\nCurrent pivot: nums[{pivot}]: {nums[pivot]}")
            # if nums[l] <= nums[r] and nums[l] < nums[pivot]:
            #     pivot = l
            #     break
            # elif nums[l] <= nums[r]:
            #     break

            m = l + ((r-l) // 2)
            if nums[m] < nums[pivot]:
                pivot = m

            print(f"l, r: {l}, {r}\nnums[{m}]: {nums[m]}")
            if nums[l] <= nums[m]:
                if nums[l] < nums[pivot]:
                    pivot = l
                l = m + 1
                # while nums[l+1] == nums[l]:
                #     l += 1
            else:
                r = m - 1
                # while nums[r-1] == nums[r]:
                #     r -= 1
        
        return pivot
        
    def binarySearch(self, nums, l, r, target) -> bool:
        while l <= r:
            m = l + ((r-l) // 2)

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return True

        return False