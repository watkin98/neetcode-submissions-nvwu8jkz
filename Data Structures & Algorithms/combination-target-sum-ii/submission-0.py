class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        seen = set()

        def dfs(i, total):
            if total == target and tuple(subset) not in seen:
                res.append(subset.copy())
                seen.add(tuple(subset))
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