class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        firstWord = strs[0]

        for i in range(0, len(firstWord)):
            char = firstWord[i]
            for j in range(1, len(strs)):
                if len(prefix) >= len(strs[j]):
                    return prefix
                elif strs[j][i] != char:
                    return prefix
                else:
                    continue

            prefix += char

        return prefix