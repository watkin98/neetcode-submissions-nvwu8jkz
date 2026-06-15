class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numMap = defaultdict(int)
        res = 0

        for num in nums:
            res += numMap[num]
            numMap[num] += 1

        return res