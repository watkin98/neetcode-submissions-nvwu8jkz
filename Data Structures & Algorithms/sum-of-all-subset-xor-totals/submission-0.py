class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        subset = []
        n = len(nums)

        def dfs(i):
            nonlocal res
            if i >= n:
                total = 0
                for num in subset:
                    total ^= num
                res += total
                return

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res

            