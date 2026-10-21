class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        expr = []

        for t in tokens:
            match t:
                case '+':
                    a, b = expr.pop(), expr.pop()
                    expr.append(a + b)
                case '-':
                    a, b = expr.pop(), expr.pop()
                    expr.append(b - a)
                case '*':
                    a, b = expr.pop(), expr.pop()
                    expr.append(a * b)
                case '/':
                    a, b = expr.pop(), expr.pop()
                    expr.append(int(b / a))
                case _:
                    expr.append(int(t))
        return expr[-1]