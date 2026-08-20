class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        res = []

        for i in range(len(s)):
            for j in range(len(strs)):
                if len(strs[j]) <= i or strs[j][i] != s[i]:
                    return "".join(res)
            res.append(s[i])

        return "".join(res)