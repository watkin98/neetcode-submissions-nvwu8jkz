class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currSum = 0
        prefixSums = defaultdict(int)
        prefixSums[0] = 1

        for num in nums:
            currSum += num
            diff = currSum - k

            res += prefixSums[diff]
            prefixSums[currSum] += 1

        return res