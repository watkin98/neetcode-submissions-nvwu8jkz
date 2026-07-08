class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = None

        for i in range(len(nums)):
            lowestVal = [float('inf'), None]
            for j in range(i+1, len(nums)):
                if nums[j] >= nums[i]:
                    continue
                
                if nums[j] < nums[i] and nums[j] < lowestVal[0]:
                    lowestVal = [nums[j], j]

            if lowestVal[0] < nums[i]:
                temp = nums[i]
                nums[i] = lowestVal[0]
                nums[lowestVal[1]] = temp
