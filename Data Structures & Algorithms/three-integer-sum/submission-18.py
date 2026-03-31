class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l_ptr = i+1
            r_ptr = n-1

            while l_ptr < r_ptr:
                sum = nums[i] + nums[l_ptr] + nums[r_ptr]

                if sum == 0:
                    res.append([nums[i], nums[l_ptr], nums[r_ptr]])
                    r_ptr -= 1
                    l_ptr += 1
                    
                    while nums[l_ptr] == nums[l_ptr-1] and l_ptr < r_ptr:
                        l_ptr += 1

                elif sum > 0:
                    r_ptr -= 1
                elif sum < 0:
                    l_ptr += 1


        return res
