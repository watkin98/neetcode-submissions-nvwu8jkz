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
            other = "".join(loop[:i]) + "".join(loop[i+1:])
            rev = loop[i][::-1]

            for _ in (loop[i], rev):
                for j in range(len(_)):
                    candidate = _[0:j] + other + _[j:]
                    if candidate > res:
                        res = candidate

        return res

