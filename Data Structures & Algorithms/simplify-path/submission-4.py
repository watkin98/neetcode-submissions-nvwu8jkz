class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        stack = []

        for c in path + '/':
            if c != '/':
                stack.append(c)
                continue
            
            if len(stack) == 1 and stack[-1] == '.':
                stack = []
                continue
            elif len(stack) == 2 and stack[-1] == '.' and stack[-2] == '.':
                if len(res) > 0:
                    res.pop()
                stack = []
                continue
            elif stack == []:
                continue
            else:
                res.append(''.join(stack))
                stack = []

        return '/' + '/'.join(res)
