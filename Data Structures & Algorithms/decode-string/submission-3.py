class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                expression = ""

                while stack[-1] != '[':
                    expression = stack.pop() + expression
                stack.pop()

                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier

                expression *= int(multiplier)
                stack.append(expression)

        return "".join(stack)