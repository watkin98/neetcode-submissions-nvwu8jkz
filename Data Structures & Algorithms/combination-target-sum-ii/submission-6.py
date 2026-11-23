class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        candidates.sort()

        def explore(i, curSum):
            if curSum == target:
                res.append(comb.copy())
                return
            if i >= len(candidates) or curSum > target:
                return

            comb.append(candidates[i])
            explore(i+1, curSum + candidates[i])

            comb.pop()
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            explore(i, curSum)

        explore(0, 0)
        return res
            