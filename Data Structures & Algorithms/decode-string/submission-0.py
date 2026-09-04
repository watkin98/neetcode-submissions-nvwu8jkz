class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                temp_str = ""
                while stack[-1] != '[':
                    temp_str = stack.pop() + temp_str
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = k + stack.pop()
                stack.append(int(k) * temp_str)

        return "".join(stack)