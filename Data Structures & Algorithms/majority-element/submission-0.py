class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        numMap = defaultdict(int)

        for num in nums:
            numMap[num] += 1

        for num in numMap:
            if numMap[num] >= majority:
                return num

        return -1


