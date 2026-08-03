class Solution:
    def validPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return self.isPalindrome(s[:L] + s[L+1:]) or self.isPalindrome(s[:R] + s[R+1:])
            L += 1
            R -= 1

        return True

    def isPalindrome(self, s) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1

        return True