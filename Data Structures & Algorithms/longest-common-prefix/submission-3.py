class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        lcf = ""
        split_strs = strs[1:]

        for i in range(len(strs[0])):
            for string in split_strs:
                if len(string) <= i or strs[0][i] != string[i]:
                    return lcf
            lcf += strs[0][i]

        return lcf