class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: #or s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False
        
        stack = []
        
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if stack == []:
                    return False

                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

        if stack == []:
            return True
        else:
            return False