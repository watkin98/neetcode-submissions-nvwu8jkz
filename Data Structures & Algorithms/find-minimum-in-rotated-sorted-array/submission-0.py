class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            print(2)
            if nums[l] < nums[r]:
                print(1)
                res = min(res, nums[l])
                break

            m = (l+r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m+1
            elif nums[m] < nums[l]:
                r = m-1

        return res