class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0

        for i, cookie in enumerate(s):
            for j, child in enumerate(g):
                if child <= cookie:
                    res += 1
                    s.pop(i)
                    g.pop(j)


        return res