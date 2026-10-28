class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
                continue

            enc_str = ""
            while stack[-1] != '[':
                enc_str = stack.pop() + enc_str
            stack.pop()
            enc_str = int(stack.pop()) * enc_str
            stack.append(enc_str)

        return "".join(stack)