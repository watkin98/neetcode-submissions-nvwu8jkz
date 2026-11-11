class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        seen = set()

        def dfs(i, total):
            check = subset.copy()
            check.sort()
            check = tuple(check)
            if total == target and check not in seen:
                res.append(subset.copy())
                seen.add(check)
                return
            if i >= len(candidates) or total > target:
                return

            subset.append(candidates[i])
            total += candidates[i]
            dfs(i+1, total)
            
            subset.pop()
            total -= candidates[i]
            dfs(i+1, total)

        dfs(0, 0)
        return res