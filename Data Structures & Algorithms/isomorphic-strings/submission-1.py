class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sASCII = []
        tASCII = []
        n = len(s)

        for i in range(n):
            sASCII.append(ord(s[i]))
            tASCII.append(ord(t[i]))

        mapping = {}

        for i in range(n):
            if sASCII[i] not in mapping:
                mapping[sASCII[i]] = tASCII[i]
            elif mapping[sASCII[i]] != tASCII[i]:
                return False

        mapping = {}
        for i in range(n):
            if tASCII[i] not in mapping:
                mapping[tASCII[i]] = sASCII[i]
            elif mapping[tASCII[i]] != sASCII[i]:
                return False

        return True