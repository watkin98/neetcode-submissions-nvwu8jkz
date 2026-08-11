class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPtr = 0

        for char in t:
            if char == s[sPtr]:
                sPtr += 1

        if sPtr == len(s):
            return True
        else:
            return False