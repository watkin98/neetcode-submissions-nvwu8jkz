class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        # Contract: Takes no input and builds a permutation with and without the element being considered (Null return)
        # Base Case: Current permutation is equal to length nums
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in nums:
                if num in perm:
                    continue
                perm.append(num)
                dfs()
                perm.pop()

        dfs()
        return res