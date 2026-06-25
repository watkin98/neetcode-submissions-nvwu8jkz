class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxIncLen = 1
        maxDecLen = 1
        incLen = 1
        decLen = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                incLen += 1
                maxIncLen = max(maxIncLen, incLen)
            else:
                maxIncLen = max(maxIncLen, incLen)
                incLen = 1
            
            if nums[i] > nums[i + 1]:
                print('-')
                decLen += 1
                maxDecLen = max(maxDecLen, decLen)
            else:
                maxDecLen = max(maxDecLen, decLen)
                decLen = 1

        print(maxIncLen)
        print(maxDecLen)
        return max(maxIncLen, maxDecLen)
