class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        ultraMax = secondMax = 0
        ultraMin = secondMin = float('inf')

        for num in nums:
            if num > ultraMax:
                ultraMax, secondMax = num, ultraMax
            elif num > secondMax:
                secondMax = num
            if num < ultraMin:
                ultraMin, secondMin = num, ultraMin
            elif num < secondMin:
                secondMin = num
                
        return (ultraMax * secondMax) - (ultraMin * secondMin)