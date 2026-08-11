class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pos = 0

        for char in t:
            if s_pos == len(s):
                break
            if char == s[s_pos]:
                s_pos += 1

        print(s_pos)
        if s_pos >= len(s) - 1:
            return True
        else:
            return False