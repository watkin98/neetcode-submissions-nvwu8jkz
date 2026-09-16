class Solution:
    def decodeString(self, s: str) -> str:
        res = []

        for c in s:
            if c != ']':
                res.append(c)
                continue

            expr = ""
            while res[-1] != '[':
                expr = res.pop() + expr
            res.pop()
            
            mult = ""
            while res and res[-1].isdigit():
                mult = res.pop() + mult

            res.append(int(mult) * expr)

        return "".join(res)