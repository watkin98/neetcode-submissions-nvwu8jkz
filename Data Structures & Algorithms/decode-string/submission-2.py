class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                temp_str = ""
                while stack[-1] != '[':
                    temp_str = stack.pop() + temp_str
                stack.pop()

                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit

                decoded_str = int(digit) * "".join(temp_str)
                stack.append(decoded_str)
            else:
                stack.append(c)

        return "".join(stack)
                