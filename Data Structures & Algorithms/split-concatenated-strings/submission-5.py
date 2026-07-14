class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        loop = []

        for string in strs:
            rev = string[::-1]
            if rev > string:
                loop.append(rev)
            else:
                loop.append(string)

        res = ""

        for i in range(len(loop)):
            other = "".join(loop[i+1:]) + "".join(loop[:i])
            rev = loop[i][::-1]
            print(f"Other: {other}")
            for _ in (loop[i], rev):
                for j in range(len(_)):
                    candidate = _[j:] + other + _[0:j]
                    #print(_)
                    print(j)
                    print(candidate)
                    if candidate > res:
                        res = candidate

        return res

