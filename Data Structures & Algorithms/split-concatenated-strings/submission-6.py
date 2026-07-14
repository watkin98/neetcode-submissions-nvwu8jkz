class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        
        for i in range(len(strs)):
            rev = strs[i][::-1]
            if rev > strs[i]:
                strs[i] = rev

        res = ""

        for i in range(len(strs)):
            mid = "".join(strs[i+1:]) + "".join(strs[:i])
            print(f"mid: {mid}")
            rev = strs[i][::-1]

            for _ in (strs[i], rev):
                for j in range(len(_)):
                    candidate = _[j:] + mid + _[:j]
                    res = max(res, candidate)
                    print(res)

        return res
