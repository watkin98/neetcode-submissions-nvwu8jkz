class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            match t:
                case '+':
                    a, b = stack.pop(), stack.pop()
                    stack.append(a + b)
                case '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                case '*':
                    a, b = stack.pop(), stack.pop()
                    stack.append(a * b)
                case '/':
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
                case _:
                    stack.append(int(t))
        return stack[-1]