class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt = dict(Counter(s1))
        s2_cnt = {}
        window = sum(s1_cnt.values())

        l = 0
        for r in range(len(s2)):
            char = s2[r]
            s2_cnt[char] = 1 + s2_cnt.get(char, 0)

            if s1_cnt == s2_cnt:
                return True

            if r-l+1 >= window:
                s2_cnt[s2[l]] -= 1
                if not s2_cnt[s2[l]]:
                    del s2_cnt[s2[l]]
                l += 1

        return False
