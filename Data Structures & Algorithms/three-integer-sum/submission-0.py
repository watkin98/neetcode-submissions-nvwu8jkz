class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        #triplet = []
        n = len(nums)

        for i in range(n):
            for j in range(n):
                for k in range (n):
                    if i == j or i == k or j == k:
                        continue
                    #elif nums[i] == nums[j] or nums[i] == nums[k] or nums [j] == nums[k]:
                    #    continue
                    else:
                        num = nums[i] + nums[j] + nums[k]
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()
                        if num == 0 and triplet not in res:
                            #print(f"triplet: {triplet}")
                            res.append(triplet)

        return res