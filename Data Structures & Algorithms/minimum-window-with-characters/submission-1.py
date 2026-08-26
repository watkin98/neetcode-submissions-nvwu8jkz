class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""

        sMap, window = {}, {}

        for c in t:
            sMap[c] = 1 + sMap.get(c, 0)

        seen, need = 0, len(sMap)
        res = [-1, -1, len(s)+1]
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in sMap and window[c] == sMap[c]:
                seen += 1

            while seen == need:
                if (r-l+1) < res[2]:
                    res = [l, r, r-l+1]

                window[s[l]] -= 1
                
                if s[l] in sMap and window[s[l]] < sMap[s[l]]:
                    seen -= 1
                l += 1

        l, r, w = res
        return s[l:r+1] if w != len(s) + 1 else ""
        