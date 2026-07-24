class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = defaultdict(int)

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in numsMap:
                return [numsMap[diff], i]
            
            numsMap[nums[i]] = i

        return [-1, -1]