class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        resultants = []

        for token in tokens:
            if token == '+':
                b, a = resultants.pop(), resultants.pop()
                result = a + b
                resultants.append(result)
            elif token == '-':
                b, a = resultants.pop(), resultants.pop()
                result = a - b
                resultants.append(result)
            elif token == '*':
                b, a = resultants.pop(), resultants.pop()
                result = b * a
                resultants.append(result)
            elif token == '/':
                b, a = resultants.pop(), resultants.pop()
                result = int(b / a)
                resultants.append(result)
            else:
                resultants.append(int(token))

        return resultants[-1]