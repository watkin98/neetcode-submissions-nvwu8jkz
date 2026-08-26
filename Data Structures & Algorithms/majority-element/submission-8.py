class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = votes = 0

        for num in nums:
            if votes == 0 and candidate != num:
                candidate = num
                continue

            if candidate == num:
                votes += 1
            else:
                votes -= 1

        return candidate
            