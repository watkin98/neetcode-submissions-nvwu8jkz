class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = [0] * 26

        for char in magazine:
            letter = ord(char) - ord('a')
            letters[letter] += 1

        for char in ransomNote:
            letter = ord(char) - ord('a')
            letters[letter] -= 1

            if letters[letter] < 0:
                return False

        return True