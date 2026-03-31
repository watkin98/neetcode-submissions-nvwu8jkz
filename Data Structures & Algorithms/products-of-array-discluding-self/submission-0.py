class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [0] * len(nums)
        product = 1

        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j:
                    product *= nums[j]

            products[i] = product
            product = 1

        return products
