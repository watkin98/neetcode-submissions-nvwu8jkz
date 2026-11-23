class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        nums.sort()
        
        def explore(i):
            if i == len(nums):
                res.append(sub.copy())
                return

            sub.append(nums[i])
            explore(i+1)

            sub.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            explore(i)

        explore(0)
        return res