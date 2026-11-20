class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        freqs = Counter(nums)
        n_elem = sum(freqs.values())

        res = []
        perm = []

        # Recursive Contract: takes in an index (i) of the current position on the candidate permutation.
        #                     Adds valid candidate when perm length equals input nums length.
        def explore(i):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in freqs:
                if freqs[num] <= 0:
                    continue

                perm.append(num)
                freqs[num] -= 1
                explore(i+1)

                perm.pop()
                freqs[num] += 1

        explore(0)
        return res
