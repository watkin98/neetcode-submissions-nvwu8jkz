class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = []
        zeros = 0

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num

        if zeros > 1:
            return [0] * len(nums)
        elif zeros == 1:
            res = [0] * len(nums)

            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = product
                    break
            return res
        else:
            res = []

            for i in range(len(nums)):
                res.append(product // nums[i])

            return res
        

        