class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = (len(nums)) // 3
        numCounter = defaultdict(int)
        res = []

        for num in nums:
            numCounter[num] += 1

        for num in numCounter:
            if numCounter[num] > freq:
                res.append(num)

        return res