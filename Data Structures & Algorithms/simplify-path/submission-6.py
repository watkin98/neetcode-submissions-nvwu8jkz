class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dir = []

        for c in path + '/':
            if c != '/':
                dir.append(c)
                continue

            if dir == []:
                continue
            elif len(dir) == 1 and dir[-1] == '.':
                dir = []
            elif len(dir) == 2 and dir[-1] == '.' and dir[-2] == '.':
                if stack:
                    stack.pop()
                dir = []
            else:
                stack.append("".join(dir))
                dir = []

        return '/' + "/".join(stack)