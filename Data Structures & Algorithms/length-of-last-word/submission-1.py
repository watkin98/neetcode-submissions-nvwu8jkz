class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        counter = 0

        while s[index] == ' ' and index >= 0:
            index -= 1

        while s[index] != ' ' and index >= 0:
            counter += 1
            index -= 1

        return counter