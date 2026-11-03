class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                s = s[1:(len(s)-1)]
                r = len(s) - 1
            else:
                break

        return len(s)
