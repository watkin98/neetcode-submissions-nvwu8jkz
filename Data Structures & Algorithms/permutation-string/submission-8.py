class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt = dict(Counter(s1))
        s2_cnt = {}

        for c in s2:
            if c in s1_cnt:
                s2_cnt[c] = 1 + s2_cnt.get(c, 0) if s2_cnt.get(c, 0) < s1_cnt[c] else 0

            if s1_cnt == s2_cnt:
                return True

        return False
