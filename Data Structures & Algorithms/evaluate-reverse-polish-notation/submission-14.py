class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                total = stack.pop() + stack.pop()
                stack.append(total)
            elif token == '-':
                diff = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(diff)
            elif token == '*':
                prod = stack.pop() * stack.pop()
                stack.append(prod)
            elif token == '/':
                res = stack[-2] / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(res))
            else:
                stack.append(int(token))

        return stack[-1]