class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l, r = 0, len(nums) - 1
        res = 0

        while l <= r and x != 0:
            left = x - nums[l]
            right = x - nums[r]

            if left < right and left >= 0:
                x -= nums[l]
                l += 1
                print(1)
            else:
                x -= nums[r]
                r -= 1
                print(2)
            res += 1
        print(x)
        return res if x == 0 else -1

