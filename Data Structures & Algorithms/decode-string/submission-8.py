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
            
            mult = ""
            while stack and stack[-1].isdigit():
                mult = stack.pop() + mult
            enc_str = int(mult) * enc_str
            stack.append(enc_str)

        return "".join(stack)