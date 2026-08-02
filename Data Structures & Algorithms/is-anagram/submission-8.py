class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = defaultdict(int)
        t_count = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_count[s[i]] += 1
            t_count[t[i]] += 1

        for key in s_count:
            if s_count[key] != t_count[key]:
                return False

        return True