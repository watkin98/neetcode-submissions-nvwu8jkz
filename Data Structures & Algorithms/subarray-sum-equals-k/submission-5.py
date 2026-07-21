class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currPfxSum = 0
        prefixSums = defaultdict(int)
        prefixSums[0] = 1

        for num in nums:
            currPfxSum += num
            diff = currPfxSum - k

            res += prefixSums[diff]
            prefixSums[currPfxSum] += 1

        return res