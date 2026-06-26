class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        satiateMap = defaultdict(int)
        g.sort()
        s.sort()
        res = 0

        for satiation in s:
            satiateMap[satiation] += 1

        print(satiateMap)
        for child in g:
            for satiation in satiateMap:
                if satiateMap[satiation] > 0 and child <= satiation:
                    res += 1
                    satiateMap[satiation] -= 1
                    break

        return res