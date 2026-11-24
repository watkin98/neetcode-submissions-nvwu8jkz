class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        par = []

        def explore(opened, closed):
            if opened == closed == n:
                res.append(''.join(par))
                return

            if opened < n:
                par.append('(')
                explore(opened + 1, closed)
                par.pop()
            if closed < opened:
                par.append(')')
                explore(opened, closed + 1)
                par.pop()

        explore(0, 0)
        return res

            