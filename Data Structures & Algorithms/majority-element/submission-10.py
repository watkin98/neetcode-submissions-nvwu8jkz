class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        votes = 1

        for i in range(1, len(nums)):
            if nums[i] == candidate:
                votes += 1
                continue

            if votes == 0:
                candidate = nums[i]
                votes = 1
            else:
                votes -= 1

        return candidate