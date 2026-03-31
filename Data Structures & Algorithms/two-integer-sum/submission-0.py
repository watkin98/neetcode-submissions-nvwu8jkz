class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        difference = None

        for i in range(0, len(nums)):
            difference = target - nums[i]

            if difference in map:
                return [map[difference], i]    
            else:
                map[nums[i]] = i
