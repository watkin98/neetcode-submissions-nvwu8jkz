class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_count = {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)

        s_count = {}
        seen, need = 0, len(t)
        l = 0
        window = [-1, -1, len(s)+1]
        for r in range(len(s)):
            c = s[r]
            s_count[c] = 1 + s_count.get(c, 0)

            if c in t_count and s_count[c] == t_count[c]:
                seen += 1

            while seen == need:
                if (r - l + 1) < window[2]:
                    window = [l, r, r-l+1]
                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    seen -= 1
                l += 1
        left, right, total = window
        return s[left:right+1] if total != len(s)+1 else ""

                
