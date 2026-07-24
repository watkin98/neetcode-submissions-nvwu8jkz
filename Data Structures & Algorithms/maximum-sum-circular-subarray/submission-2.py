class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum, minSum = nums[0], nums[0]
        curMaxSum, curMinSum = 0, 0
        total = 0

        for num in nums:
            if curMaxSum < 0:
                curMaxSum = 0
            if curMinSum > 0:
                curMinSum = 0
            curMaxSum += num
            curMinSum += num
            maxSum = max(maxSum, curMaxSum)
            minSum = min(minSum, curMinSum)
            total += num

        if maxSum > total - minSum:
            return maxSum
        elif maxSum < 0:
            return maxSum
        else:
            return total - minSum