class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = tally = 0

        for num in nums:
            if num == candidate:
                tally += 1
            elif num != candidate and tally == 0:
                candidate = num
                tally = 1
            else:
                tally -= 1
        
        return candidate