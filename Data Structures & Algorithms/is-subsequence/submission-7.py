class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        if len(s) == 0:
            return True

        n = len(s)
        i = 0

        for char in t:
            if char == s[i]:
                i += 1

            if i == n:
                return True

        return False