class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        comparison = strs[0]
        res = []

        for i in range(len(comparison)):
            for j in range(len(strs)):
                if len(strs[j]) < i or comparison[i] != strs[j][i]:
                    return "".join(res)
            res.append(comparison[i])
        
        return "".join(res)