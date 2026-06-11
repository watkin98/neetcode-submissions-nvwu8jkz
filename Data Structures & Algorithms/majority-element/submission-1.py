class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        numMap = defaultdict(int)

        for num in nums:
            numMap[num] += 1

        res = nums[0]
        for num in numMap:
            if numMap[num] >= majority and numMap[num] > numMap[res]:
                res = num

        return res


