class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        r = len(s) - 1

        while s[r] == ' ' and r >= 0:
            r -= 1

        while s[r] != ' ' and r >= 0:
            length += 1
            r -= 1

        return length