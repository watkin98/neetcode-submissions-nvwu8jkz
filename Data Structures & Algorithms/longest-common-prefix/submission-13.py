class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        compare = strs[0]
        res = []

        for i in range(len(compare)):
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[j][i] != compare[i]:
                    return ''.join(res)

            res.append(compare[i])

        return ''.join(res)


