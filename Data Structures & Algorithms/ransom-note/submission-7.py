class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterCount = defaultdict(int)

        for char in magazine:
            letterCount[char] += 1

        for char in ransomNote:
            if letterCount[char] == 0:
                return False
            letterCount[char] -= 1

        return True