class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        s_pos = 0
        
        for char in t:
            if s_pos == len(s):
                break
            if char == s[s_pos]:
                s_pos += 1

        print(s_pos)
        if s_pos >= len(s):
            return True
        else:
            return False