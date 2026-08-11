class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        for i in range(n):
            l = i + 1
            r = i + 2

            while r < n:
                if (nums[i] + nums[l] + nums[r]) == 0:
                    triplet = [nums[i], nums[l], nums[r]]
                    triplet.sort()

                    if triplet not in res:
                        res.append(triplet)

                l += 1
                r += 1

        return res