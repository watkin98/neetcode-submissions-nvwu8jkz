class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        
        for i in range(len(strs)):
            rev = strs[i][::-1]
            if rev > strs[i]:
                strs[i] = rev

        res = ""
        for i in range(len(strs)):
            other = "".join(strs[i+1:]) + "".join(strs[:i])
            rev = strs[i][::-1]
            for string in (strs[i], rev):
                for j in range(len(string)):
                    candidate = string[j:] + other + string[:j]
                    res = max(res, candidate)

        return res