class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        if len(s) > len(t):
            return False

        s_counter = 0

        for char in t:
            if s_counter == len(s) - 1:
                return True
                
            if char == s[s_counter]:
                s_counter += 1


        return False