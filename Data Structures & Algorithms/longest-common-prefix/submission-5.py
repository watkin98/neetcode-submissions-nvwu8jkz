class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # setup initial variables to store the character element being compared,
        # a boolean that tracks when the shortest string has been reached, and 
        # the resulting prefix
        charCompare = 0
        isShortestStringReached = False
        prefix = ""

        if strs == []:
            return ""

        # loop while the shortest string has not been reached (boolean is false)
        while isShortestStringReached is False:

            # enumerate through the list of strings to check if the 
            # character being compared exists in each string at the expected
            # index. 
            for string in strs:

                # flip boolean if shortest string has been reached or if char being compared
                # does not exist in one of the strings, then break out of enumeration. 
                if len(string) < charCompare + 1:
                    isShortestStringReached = True
                    break
                elif string[charCompare] != strs[0][charCompare]:
                    isShortestStringReached = True
                    break
            # if boolean still false, add char to prefix and increment charCompare
            if isShortestStringReached is False:
                prefix += strs[0][charCompare]
                charCompare += 1

        # return resulting prefix
        return prefix


