class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # L = 0
        # k = 1

        # for R in range(1, len(nums) - 1):
        #     if nums[L] == nums[R]:
        #         nums[R] = nums[R+1]
        #         k += 1
        #         L += 1
        # print(nums)
        # return k
        numSet = set(nums)
        listNums = list(numSet)
        listNums.sort()
        for i in range(len(listNums)):
            nums[i] = listNums[i]

        return len(listNums)