class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = [0] * 26

        for char in magazine:
            letter = ord(char) - ord('a')
            chars[letter] += 1

        for char in ransomNote:
            letter = ord(char) - ord('a')
            chars[letter] -= 1

            if chars[letter] < 0:
                return False

        return True