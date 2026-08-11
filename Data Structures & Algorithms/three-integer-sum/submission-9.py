class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        l_ptr = 0
        r_ptr = 0
        n = len(nums)

        for i in range(n):
            l_ptr = i+1
            r_ptr = n-1
            
            #if i != n-1 and nums[i] == nums[i+1]:
            #    continue

            while l_ptr < r_ptr:
                sum = nums[i] + nums[l_ptr] + nums[r_ptr]

                if sum == 0: #and [nums[i], nums[l_ptr], nums[r_ptr]] not in res:
                    res.append([nums[i], nums[l_ptr], nums[r_ptr]])
                    break
                elif sum > 0:
                    r_ptr -= 1
                elif sum < 0:
                    l_ptr += 1


        return res
