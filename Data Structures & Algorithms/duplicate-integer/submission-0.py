class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for num in nums:
            if num in map:
                return True
            else:
                map[num] = None

        return False