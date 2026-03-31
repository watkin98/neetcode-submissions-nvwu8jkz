class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        result = [0] * len(nums)
        zeros = 0

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                totalProduct *= num
            
        if zeros > 1:
            return [0] * len(nums)
        elif zeros == 1:
            for i in range(0, len(nums)):
                if nums[i] != 0:
                    result[i] = 0
                else:
                    result[i] = totalProduct
            return result
        else:
            for i in range(0, len(nums)):
                result[i] = totalProduct // nums[i]

            return result