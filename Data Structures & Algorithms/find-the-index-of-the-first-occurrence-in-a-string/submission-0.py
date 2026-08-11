class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] != needle[0]:
                continue
            
            iSubstr = i
            for char in needle:
                if iSubstr > len(haystack) - 1:
                    return -1
                if haystack[iSubstr] != char:
                    break
                iSubstr += 1

            return i

        return -1