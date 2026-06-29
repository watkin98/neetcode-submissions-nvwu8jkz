class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        isMonoInc = True
        isMonoDec = True
        for i in range(0, len(nums) - 1):
            if isMonoInc and nums[i] > nums[i+1]:
                isMonoInc = False
    
            if isMonoDec and nums[i] < nums[i+1]:
                isMonoDec = False

            if isMonoInc is False and isMonoDec is False:
                return False
        
        return True