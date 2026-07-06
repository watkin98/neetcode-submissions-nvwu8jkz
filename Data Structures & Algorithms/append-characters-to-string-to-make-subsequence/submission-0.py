class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_ptr, t_ptr = 0, 0

        while s_ptr < len(s) and t_ptr < len(t):
            if t[t_ptr] == s[s_ptr]:
                t_ptr += 1
            s_ptr += 1

        if t_ptr == len(t):
            return 0
        else: #s_ptr == len(s):
            return len(t) - t_ptr

        