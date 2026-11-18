class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        combs = math.factorial(n)
        output = [[None] * n for _ in range(combs)]

        for row in range(combs):
            available = nums.copy()

            for i in range(n):
                step_size = math.factorial(n - i - 1)

                digit = (row // step_size) % (n - i)

                output[row][i] = available.pop(digit)

        return output