class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        comparisonWord = strs[0]
        charIndex = 0

        for i in range(0, len(comparisonWord)):
            for j in range(1, len(strs)):
                if len(strs[j]) - 1 < charIndex or comparisonWord[charIndex] != strs[j][charIndex]:
                    return prefix

            prefix += comparisonWord[charIndex]
            charIndex += 1

        return prefix