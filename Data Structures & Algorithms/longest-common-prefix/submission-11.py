class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        starter = strs[0]

        for i in range(len(starter)):
            for word in strs:
                if i >= len(word) or starter[i] != word[i]:
                    return res
            res += starter[i]

        return res
