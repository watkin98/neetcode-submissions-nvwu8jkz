class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        operands = []
        
        for token in tokens:
            match token:
                case '+':
                    for _ in range(len(operands)):
                        res += operands.pop()
                case '-':
                    for _ in range(len(operands)):
                        res -= operands.pop()
                case '*':
                    for _ in range(len(operands)):
                        res *= operands.pop()
                case '/':
                    for _ in range(len(operands)):
                        res /= operands.pop()
                case _:
                    operands.append(int(token))
        return res

            