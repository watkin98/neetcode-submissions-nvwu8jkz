class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        sub_path = []

        for c in path + '/':

            if c == '/':
                if not stack and not sub_path:
                    ##print(1)
                    continue
                elif sub_path == ['.', '.']:
                    ##print(2)
                    if stack != []:
                        stack.pop()
                    sub_path = []
                elif sub_path == ['.']:
                    ##print(3)
                    sub_path = []
                else:
                    ##print(4)
                    if sub_path != []:
                        stack.append(''.join(sub_path))
                    sub_path = []
            else:
                ###print(5)
                sub_path.append(c)

            print(f"stack: {stack}\nsub-path: {sub_path}\n")

        return "/" + "/".join(stack)