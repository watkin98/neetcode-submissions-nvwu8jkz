class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        numSet = set()
        maxSum = -1

        for num in nums:
            diff = k - num

            for item in numSet:
                if num + item < k:
                    maxSum = max(maxSum, num + item)
            numSet.add(num)

        return maxSum