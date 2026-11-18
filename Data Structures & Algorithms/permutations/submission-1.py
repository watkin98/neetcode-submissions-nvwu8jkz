class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        p = []

        def dfs():
            if len(p) == len(nums):
                res.append(p.copy())
                return

            for num in nums:
                if num in p:
                    continue
                p.append(num)
                dfs()
                p.pop()

        dfs()
        return res
