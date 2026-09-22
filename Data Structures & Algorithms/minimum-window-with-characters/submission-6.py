class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_count = defaultdict(int)
        t_counter = 0
        for c in t:
            t_count[c] += 1
            t_counter += 1

        s_count = defaultdict(int)
        seen, need = 0, t_counter
        l = 0
        res = (-1, -1, float('inf'))
        for r in range(len(s)):
            char = s[r]

            if char in t_count:
                s_count[char] += 1
                seen += 1 if s_count[char] <= t_count[char] else 0

            while seen == need:
                if (r-l+1) < res[2]:
                    res = (l, r, r-l+1)

                char_l = s[l]

                if char_l in s_count:
                    s_count[char_l] -= 1
                    if s_count[char_l] < t_count[char_l]:
                        seen -= 1
                l += 1

        l, r, length = res

        return s[l:r+1] if length != float('inf') else ""