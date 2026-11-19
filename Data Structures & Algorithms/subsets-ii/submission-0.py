class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()     # Sort the input to enable easy duplicate skipping
        res = []
        subset = []

        # Recursive Contract: takes in index (i); returns when index is outside
        #                     of array boundaries. Null return value.
        def explore(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            explore(i+1)

            subset.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            explore(i)

        explore(0)
        return res
            