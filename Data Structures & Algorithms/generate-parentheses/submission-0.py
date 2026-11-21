class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        candidate = []

        # Recursive Call: Passes in the number of parentheses used to generate the candidate at that call. Appends
        #                 a candidate to the collection (res) when the number of parentheses used equals n (i == n)
        def explore(open, closed):
            if open == closed == n:
                res.append(''.join(candidate))
                return

            # Decision: choose to place an open parenthesis or closed parenthesis
            if open < n:
                candidate.append('(')
                explore(open + 1, closed)
                candidate.pop()
            if closed < open:
                candidate.append(')')
                explore(open, closed + 1)
                candidate.pop()

        explore(0, 0)
        return res