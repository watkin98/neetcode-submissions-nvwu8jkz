class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i, hay in enumerate(haystack):
            if hay != needle[0]:
                continue

            index = i
            needleFound = True
            for needling in needle:
                if index == len(haystack) or needling != haystack[index]:
                    needleFound = False
                    break
                index += 1
            if needleFound:
                return i

        return -1