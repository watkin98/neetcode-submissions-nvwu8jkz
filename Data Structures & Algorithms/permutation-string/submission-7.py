class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        k = len(s1)

        s1Map = defaultdict(int)
        for c in s1:
            s1Map[c] += 1

        s2Map = defaultdict(int)

        l = 0
        for r in range(len(s2)):
            c = s2[r]

            s2Map[c] += 1
            if r-l+1 != k:
                continue

            if s2Map == s1Map:
                return True

            c_at_l = s2[l]
            s2Map[c_at_l] -= 1
            l += 1

            if s2Map[c_at_l] == 0:
                del s2Map[c_at_l]

        return s2Map == s1Map