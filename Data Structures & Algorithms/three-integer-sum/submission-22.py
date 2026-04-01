class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        #print(f"nums: {nums}")

        for i, a in enumerate(nums):
            l = i+1
            r = len(nums) - 1
            #print(f"i: {i}")
            while l < r:
                sum = a + nums[l] + nums[r]
                #print(f"[a, l, r]: [{a}, {nums[l]}, {nums[r]}] \nsum: {sum}")
                if sum > 0:
                    r -= 1
                    continue
                elif sum < 0:
                    l += 1
                    continue
                else:
                    if [a, nums[l], nums[r]] not in res:
                        res.append([a, nums[l], nums[r]])
                    l += 1

        return res