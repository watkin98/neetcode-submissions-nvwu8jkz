class Solution:
    def decodeString(self, s: str) -> str:
        expression = []

        for c in s:
            if c != ']':
                expression.append(c)
                continue

            curr_expression = ""
            while expression[-1] != '[':
                curr_expression = expression.pop() + curr_expression
            expression.pop()    # pop the '[' now that it's been found

            multiplier = ""
            while expression and expression[-1].isdigit():
                multiplier = expression.pop() + multiplier
            
            expression.append(int(multiplier) * curr_expression)
            
        return "".join(expression)