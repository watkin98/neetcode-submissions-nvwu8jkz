class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        seen = set()

        def explore():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in nums:
                if num not in seen:
                    perm.append(num)
                    seen.add(num)
                    explore()

                    perm.pop()
                    seen.remove(num)

        explore()
        return res
                