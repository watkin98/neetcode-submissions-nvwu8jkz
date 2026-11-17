class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        c = []

        # helper contract: goes through the numbers [1, n] and chooses to include or not include a number 
        #                  for combinations c
        def dfs(i):
            if i == 0:
                return
            
            c.append(i)
            if len(c) == k:
                res.append(c.copy())
            dfs(i-1)


            c.pop()
            if len(c) == k:
                if res[-1] != c:
                    res.append(c.copy())
            dfs(i-1)

        dfs(n)
        return res