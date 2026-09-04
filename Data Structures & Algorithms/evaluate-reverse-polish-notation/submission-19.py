class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case '+':
                    a, b = stack.pop(), stack.pop()
                    res = a + b
                    stack.append(res)
                case '-':
                    a, b = stack.pop(), stack.pop()
                    res = b - a
                    stack.append(res)
                case '*':
                    a, b = stack.pop(), stack.pop()
                    res = a * b
                    stack.append(res)
                case '/':
                    a, b = stack.pop(), stack.pop()
                    res = b // a
                    stack.append(int(res))
                case _:
                    stack.append(int(token))

        return stack[0]