class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] != needle[0]:
                continue
            
            iSubstr = i
            notFound = False
            for char in needle:
                if iSubstr > len(haystack) - 1:
                    return -1
                if haystack[iSubstr] != char:
                    notFound = True
                    break
                iSubstr += 1

            if notFound == False:
                return i
            i = iSubstr

        return -1