class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = {}

        for char in s1:
            s1_chars[char] = s1_chars[char] + 1 if char in s1_chars else 1

        l = 0
        s1_chars_copy = s1_chars.copy()
      
        for r in range(len(s2)):
            if s2[r] in s1_chars_copy and s1_chars_copy[s2[r]] > 0:
                s1_chars_copy[s2[r]] -= 1

                if list(s1_chars_copy.values()) == [0] * len(s1_chars_copy.keys()):
                    return True
            elif s2[r] in s1_chars_copy and s1_chars_copy[s2[r]] <= 0:
                l = r
                s1_chars_copy = s1_chars.copy()
            elif s2[r] not in s1_chars_copy and l != r:
                l = r
                s1_chars_copy = s1_chars.copy()

        return False

