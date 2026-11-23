class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        seen = set()

        def explore(i):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            if i == len(nums):
                return

            for num in nums:
                if num not in seen:
                    perm.append(num)
                    seen.add(num)
                    explore(i+1)

                    perm.pop()
                    seen.remove(num)

        explore(0)
        return res
                