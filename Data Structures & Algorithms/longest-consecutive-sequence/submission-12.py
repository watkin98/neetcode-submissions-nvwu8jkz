class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        nums.sort()
        LCS = 1
        counter = 1

        print(nums)
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i] - 1:
                counter += 1
            elif nums[i - 1] == nums[i]:
                continue
            else:
                LCS = max(counter, LCS)
                counter = 1

        
        return max(LCS, counter)