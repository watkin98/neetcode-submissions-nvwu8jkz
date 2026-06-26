class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxIncreasingLen = 1
        maxDecreasingLen = 1
        currIncreasingLen = 1
        currDecreasingLen = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                currIncreasingLen += 1
                maxIncreasingLen = max(maxIncreasingLen, currIncreasingLen)
            else:
                currIncreasingLen = 1

            if nums[i] > nums[i + 1]:
                currDecreasingLen += 1
                maxDecreasingLen = max(maxDecreasingLen, currDecreasingLen)
            else:
                currDecreasingLen = 1

        return max(maxIncreasingLen, maxDecreasingLen)