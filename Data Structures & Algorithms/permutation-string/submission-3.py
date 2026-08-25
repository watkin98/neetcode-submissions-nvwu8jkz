class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freq = [0] * 26
        for char in s1:
            index = ord(char) - ord('a')
            s1freq[index] += 1

        s2WindowFreq = [0] * 26
        l = 0
        for r in range(len(s2)):
            if r < len(s1):
                index = ord(s2[r]) - ord('a')
                s2WindowFreq[index] += 1
                continue

            if s2WindowFreq == s1freq:
                return True

            index = ord(s2[r]) - ord('a')
            s2WindowFreq[index] += 1

            index = ord(s2[l]) - ord('a')
            s2WindowFreq[index] -= 1
            l += 1

        return s2WindowFreq == s1freq
            

            
