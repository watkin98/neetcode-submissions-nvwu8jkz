class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        isMono = True
        for i in range(0, len(nums) - 1):
            if nums[i] != nums[i+1] and nums[i] + 1 != nums[i+1]:
                isMono = False
                break

        if isMono:
            print(1)
            return True

        isMono = True
        for i in range(0, len(nums) - 1):
            if nums[i] != nums[i+1] and nums[i] - 1 != nums[i+1]:
                isMono = False
                break

        print(2)
        return isMono