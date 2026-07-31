class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        prefixSum = []

        for num in nums:
            total += num
            prefixSum.append(total)

        # if total > 2 and (total / 2) % 2 == 1:
        #     # print(total / 2)
        #     # print(1)
        #     return -1

        for i in range(len(prefixSum)):
            #print(f"prefixSum[{i}]: {prefixSum[i]}\nPivot Value: {pivotValue}")
            #print(f"i: {i}\nnums:      {nums}\nprefixSum: {prefixSum}")
            leftSum = prefixSum[i-1] if i > 0 else 0
            rightSum = prefixSum[len(prefixSum)-1] - prefixSum[i]
            print(f"leftSum: {leftSum}\nrightSum: {rightSum}")
            if leftSum == rightSum:
                return i
            # if prefixSum[i] > (total / 2):
            #     return -1

        return -1