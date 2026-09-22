class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
                continue

            expression = ""

            while stack[-1] != '[':
                expression = stack.pop() + expression
            stack.pop()

            multiplier = ""
            while stack and stack[-1].isdigit():
                multiplier = stack.pop() + multiplier
            
            stack.append(int(multiplier) * expression)

        return "".join(stack)