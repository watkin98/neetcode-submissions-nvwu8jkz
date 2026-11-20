class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        frqs = Counter(nums)

        res = []
        perm = []

        def explore(i):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in frqs:
                if frqs[num] == 0:
                    continue

                perm.append(num)
                frqs[num] -= 1
                explore(i+1)

                perm.pop()
                frqs[num] += 1

        explore(0)
        return res