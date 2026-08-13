class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = defaultdict(int)
        t_count = defaultdict(int)
        n = len(t)

        for i in range(n):
            s_count[s[i]] += 1
            t_count[t[i]] += 1

        return s_count == t_count