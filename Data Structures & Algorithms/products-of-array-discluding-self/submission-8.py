class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = [0] * len(nums)
        riteProd = [0] * len(nums)
        res = [0] * len(nums)

        leftProd[0] = 1
        riteProd[len(nums) - 1] = 1

        for i in range(1, len(nums)):
            leftProd[i] = leftProd[i - 1] * nums[i - 1]

        print(leftProd)
        for i in range(len(nums) - 2, -1, -1):
            riteProd[i] = riteProd[i + 1] * nums[i + 1]

        print(riteProd)
        for i in range(0, len(nums)):
            res[i] = leftProd[i] * riteProd[i]

        return res