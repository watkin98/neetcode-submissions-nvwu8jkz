class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            if haystack[i] != needle[0]:
                continue
            
            isFound = True
            i_needle = i
            for char in needle:
                if i_needle >= len(haystack) or char != haystack[i_needle]:
                    isFound = False
                    break
                i_needle += 1

            if isFound:
                return i
            else:
                i = i_needle

        return -1