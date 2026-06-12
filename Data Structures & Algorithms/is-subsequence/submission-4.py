class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        sPtr = 0

        for char in t:
            if sPtr < len(s) and char == s[sPtr]:
                sPtr += 1

        if sPtr == len(s):
            return True
        else:
            return False