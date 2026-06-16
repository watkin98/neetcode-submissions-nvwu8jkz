class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        if s == "":
            return True

        counter = 0

        for char in t:
            if s[counter] == char:
                counter += 1

            if counter == len(s):
                return True

        return False