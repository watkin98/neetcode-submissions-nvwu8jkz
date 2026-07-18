class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = sum = 0
        prefixSums = defaultdict(int)

        for num in nums:
            prefixSums[sum] += 1
            sum += num
            res += prefixSums[sum - k]

        return res