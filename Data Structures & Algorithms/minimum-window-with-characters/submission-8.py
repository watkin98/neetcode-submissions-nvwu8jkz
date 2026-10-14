class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnt = dict(Counter(t))
        s_cnt = {}

        seen, need = 0, sum(t_cnt.values())
        res = ("", float('inf'))

        l = 0
        for r in range(len(s)):
            char = s[r]
            if char in t_cnt:
                s_cnt[char] = 1 + s_cnt.get(char, 0)
                seen += 1 if s_cnt[char] <= t_cnt[char] else 0

                while seen == need:
                    if r-l+1 < res[1]:
                        res = (s[l:r+1], r-l+1)
                    
                    if s[l] in s_cnt:
                        s_cnt[s[l]] -= 1
                        seen -= 1 if s_cnt[s[l]] < t_cnt[s[l]] else 0
                    l += 1

        return res[0]
        