class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        prefixSum = []

        for num in nums:
            total += num
            prefixSum.append(total)

        if (total / 2) % 1 != 0:
            return -1

        for i in range(len(prefixSum)):
            leftSum = prefixSum[i-1] if i > 0 else 0
            rightSum = prefixSum[len(prefixSum)-1] - prefixSum[i]

            if leftSum == rightSum:
                return i

        return -1