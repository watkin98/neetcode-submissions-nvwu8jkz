class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        seen = Counter(nums)

        def explore():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in seen:
                if seen[num] != 0:
                    perm.append(num)
                    seen[num] -= 1
                    explore()

                    perm.pop()
                    seen[num] += 1

        explore()
        return res