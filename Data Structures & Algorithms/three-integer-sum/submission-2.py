class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        map = {}

        for i in range(n):
            for j in range(i+1, n):
                sum = nums[i] + nums[j]
                map[sum] = (i, j, sum)

        for k in range(n):
            for sum in map:
                if (sum + nums[k]) == 0 and k != map[sum][0] and k != map[sum][1]:
                    triplet = [nums[map[sum][0]], nums[map[sum][1]], nums[k]]
                    triplet.sort()
                    if triplet not in res:
                        res.append(triplet)
                    
        return res
        # for item in map:
        #    print(f"Mapping: {map[item]}")