class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs[0] == "":
            return ""

        charCompare = 0
        isStrLenExceeded = False
        res = ""

        while isStrLenExceeded is False:
            for string in strs:
                if charCompare >= len(string):
                    isStrLenExceeded = True
                    break
                elif string[charCompare] != strs[0][charCompare]:
                    isStrLenExceeded = True
                    break

            if isStrLenExceeded is False:    
                res += strs[0][charCompare]
                charCompare += 1

        return res

