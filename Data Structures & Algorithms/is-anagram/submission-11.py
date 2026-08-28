class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqS = [0] * 26
        freqT = [0] * 26

        for i in range(len(s)):
            charS = ord(s[i]) - ord('a')
            charT = ord(t[i]) - ord('a')

            freqS[charS] += 1
            freqT[charT] += 1
            
        return freqS == freqT