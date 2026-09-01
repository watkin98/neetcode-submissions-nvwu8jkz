class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        expression = []

        for c in path + '/':
            if c != '/':
                expression.append(c)
                continue
            
            if len(expression) == 1 and expression == ['.']:
                expression = []
            elif len(expression) == 2 and expression == ['.', '.']:
                stack.pop() if len(stack) > 0 else None
                expression = []
            elif len(expression) == 0:
                continue
            else:
                stack.append("".join(expression))
                expression = []
                
        return '/' + '/'.join(stack)