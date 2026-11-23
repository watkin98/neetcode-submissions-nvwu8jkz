class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def explore(i, curSum):
            if i == len(nums):
                return
            if curSum > target:
                return
            if curSum == target:
                res.append(comb.copy())
                return

            comb.append(nums[i])
            explore(i, curSum + nums[i])

            comb.pop()
            explore(i+1, curSum)

        explore(0,0)
        return res
            