class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def explore(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            explore(i+1)

            subset.pop()
            explore(i+1)

        explore(0)
        return res