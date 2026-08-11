class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        for i in range(n):
            for l in range(i+1, n):
                for r in range (i+2, n):
                    if (nums[i] + nums[l] + nums[r]) == 0:
                        triplet = [nums[i], nums[l], nums[r]]
                        triplet.sort()

                        if triplet not in res:
                            res.append(triplet)

        return res