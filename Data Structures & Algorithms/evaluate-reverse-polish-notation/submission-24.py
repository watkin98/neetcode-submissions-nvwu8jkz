class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        expression = []

        for t in tokens:
            match t:
                case '+':
                    b, a = expression.pop(), expression.pop()
                    expression.append(a + b)
                case '-':
                    b, a = expression.pop(), expression.pop()
                    expression.append(a - b)
                case '*':
                    b, a = expression.pop(), expression.pop()
                    expression.append(a * b)
                case '/':
                    b, a = expression.pop(), expression.pop()
                    expression.append(a // b)
                case _:
                    expression.append(int(t))

        return expression[-1]