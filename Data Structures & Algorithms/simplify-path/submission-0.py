class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = []

        for c in path + '/':
            if c == '/':
                if curr == [".", "."]:
                    if stack:
                        stack.pop()
                elif curr != [] and curr != ["."]:
                    stack.append(''.join(curr))
                curr = []
            else:
                curr.append(c)

        return '/' + '/'.join(stack)