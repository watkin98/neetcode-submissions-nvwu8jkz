class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        pairs = defaultdict(int)

        for num in nums:
            res += pairs[num]
            pairs[num] += 1

        return res