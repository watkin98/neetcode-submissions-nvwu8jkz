class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_chars = [0] * 26
        s2_chars = [0] * 26
        for char in s1:
            s1_chars[ord(char) - ord('a')] += 1

        for i in range(len(s1)):
            index = ord(s2[i]) - ord('a')
            s2_chars[index] += 1

        l = 0
        for r in range(len(s1), len(s2)):
            print(f"s2_chars before: {s2_chars}")
            if s1_chars == s2_chars:
                return True

            char_i = ord(s2[r]) - ord('a')
            s2_chars[char_i] += 1
            s2_chars[ord(s2[l]) - ord('a')] -= 1
            l += 1
            print(f"s2_chars after: {s2_chars}")

        return s1_chars == s2_chars
