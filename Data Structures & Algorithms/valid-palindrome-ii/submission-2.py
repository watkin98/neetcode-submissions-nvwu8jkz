class Solution:
    def validPalindrome(self, s: str) -> bool:
        deleteUsed = False
        L, R = 0, len(s) - 1

        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
                continue

            if deleteUsed:
                return False

            if s[R-1] == s[L]:
                s = s[:R] + s[R+1:]
                R -= 1
            elif s[L+1] == s[R]:
                s = s[:L] + s[L+1:]
                R -= 1
            else:
                return False
            deleteUsed = True

        return True
