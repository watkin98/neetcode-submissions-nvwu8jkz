class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        LCS = 0

        for num in nums:
            if (num - 1) not in numSet:
                counter = 1
                while (num + counter) in numSet:
                    counter += 1
                LCS = max(LCS, counter)

        return LCS