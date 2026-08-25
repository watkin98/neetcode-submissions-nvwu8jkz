class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path[1:]
        stack = []
        expression = []

        for c in path + '/':
            if c == '/':
                if len(expression) == 2 and expression[-1] == '.' and expression[-2] == '.':
                    if stack:
                        stack.pop()
                    expression = []
                elif len(expression) == 1 and expression[-1] == '.':
                    expression = []
                elif expression == []:
                    continue
                else:
                    path = "".join(expression)
                    stack.append(path)
                    expression = []
            else:
                expression.append(c)

        return '/' + '/'.join(stack)