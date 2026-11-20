class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        seen = set()

        # Recursive Contract: Takes no input. Builds permutation candidates and appends valid 
        #                     candidates to collection res. Decides to include a value from nums
        #                     if it has not been used yet, using set seen as reference.
        def explore():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in nums:
                if num in seen:
                    continue

                perm.append(num)
                seen.add(num)
                explore()

                perm.pop()
                seen.remove(num)

        explore()
        return res