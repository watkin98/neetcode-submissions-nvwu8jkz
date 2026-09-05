class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1
        
        s_count = defaultdict(int)
        seen, need = 0, len(t)
        l = 0
        res = [-1, -1, len(s) + 1]
        for r in range(len(s)):
            c = s[r]

            if c in t_count and s_count[c] < t_count[c]:
                s_count[c] += 1
                seen += 1
            elif c in t_count:
                s_count[c] += 1
            
            while seen == need:
                if (r-l+1) < res[2]:
                    res = [l, r, r-l+1]

                if s[l] in s_count and s_count[s[l]] - 1 < t_count[s[l]]:
                    s_count[s[l]] -= 1
                    seen -= 1
                elif s[l] in s_count:
                    s_count[s[l]] -= 1
                l += 1

        left, right, length = res
        return s[left:right+1] if length != len(s) + 1 else ""