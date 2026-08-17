class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                total = stack.pop() + stack.pop()
                stack.append(total)
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                diff = b - a
                stack.append(diff)
            elif token == '*':
                prod = stack.pop() * stack.pop()
                stack.append(prod)
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                res = b / a
                stack.append(int(res))
            else:
                stack.append(int(token))

        return stack[-1]