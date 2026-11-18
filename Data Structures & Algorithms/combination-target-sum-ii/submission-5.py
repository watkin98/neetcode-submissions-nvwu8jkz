class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidate = []
        candidates.sort()

        # Recursive Contract: take in the current index and current sum from previous indices and 
        #                     decision points and check if they sum to target. Null return.
        def dfs(i, curSum):
            if curSum == target:
                res.append(candidate.copy())
                return
            if i >= len(candidates):
                return
            if curSum > target:
                return

            candidate.append(candidates[i])
            dfs(i+1, curSum + candidates[i])

            candidate.pop()
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            dfs(i, curSum)

        dfs(0, 0)
        return res
            
