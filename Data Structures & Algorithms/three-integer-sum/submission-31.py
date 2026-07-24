class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):

            if num > 0:
                break

            if i > 0 and num == nums[i-1]:
                continue

            L, R = i + 1, len(nums) - 1

            while L < R:
                threeSum = num + nums[L] + nums[R]

                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    res.append([num, nums[L], nums[R]])
                    R -= 1
                    L += 1
                    while nums[L] == nums[L-1] and L < R:
                        L += 1

        return res

