class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        expression = []

        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                res = self.arithmetic(expression.pop(), expression.pop(), token)
                expression.append(res)
            else:
                expression.append(token)
        return expression.pop()


    def arithmetic(self, a, b, op) -> int:
        if op == '+':
            return int(a) + int(b)
        elif op == '-':
            return int(a) - int(b)
        elif op == '*':
            return int(a) * int(b)
        elif op == '/':
            return int(a) // int(b)
        else:
            return -1