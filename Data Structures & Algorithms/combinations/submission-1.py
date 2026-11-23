class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []

        def explore(i):
            if len(comb) == k:
                res.append(comb.copy())
                return
            if i > n:
                return
            
            comb.append(i)
            explore(i+1)

            comb.pop()
            explore(i+1)

        explore(1)
        return res
            