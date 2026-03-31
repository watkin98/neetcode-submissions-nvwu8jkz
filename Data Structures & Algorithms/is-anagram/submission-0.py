class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMapS = {}
        charMapT = {}

        for char in s:
            if char in charMapS:
                charMapS[char] += 1
            else:
                charMapS[char] = 1

        for char in t:
            if char in charMapT:
                charMapT[char] += 1
            else:
                charMapT[char] = 1

        if charMapS == charMapT:
            return True
        else:
            return False
        