class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, votes = nums[0], 1

        for i in range(1, len(nums)):
            if nums[i] == candidate:
                votes += 1
            elif votes > 0:
                votes -= 1
            else:
                candidate = nums[i]
                votes += 1

        return candidate