class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        terms = []

        def dfs(i):
            if sum(terms) == target:
                res.append(terms.copy())
                return
            if sum(terms) > target or i >= len(nums):
                return

            terms.append(nums[i])
            dfs(i)
            terms.pop()
            dfs(i+1)

        dfs(0)
        return res