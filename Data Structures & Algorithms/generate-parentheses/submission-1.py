class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        out = []
        gen = ""
        flipper = {'(' : ')', ')' : '('}

        for i in range(n):
            gen += "()"
        
        def recurse(s: str, idx: int) -> None:            
            out.append(s)
            if len(s) - idx < 2:
                return
            for i in range(idx, len(s) - 2):
                p = s[i - 1]
                l = s[i]
                r = s[i + 1]
                if l == ')' and r == "(":
                    ns = s[:i] + "()" + s[i + 2:]
                    if p == l:
                        recurse(ns, i - 1)
                    else:
                        recurse(ns, i + 1)
        
        recurse(gen, 1)
        
        return out