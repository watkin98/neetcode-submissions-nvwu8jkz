class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = [0] * 26
        for c in s1:
            key = ord(c) - ord('a')
            s1_map[key] += 1

        s2_map = [0] * 26
        l = 0
        for r in range(len(s2)):
            key = ord(s2[r]) - ord('a')
            if not s1_map[key]:
                s2_map = [0] * 26
                l = r + 1
                continue
            
            s2_map[key] += 1

            if s2_map == s1_map:
                return True

        return False