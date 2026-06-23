class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charCount = defaultdict(int)

        for char in magazine:
            charCount[char] += 1

        for char in ransomNote:
            if charCount[char] == 0:
                return False
            charCount[char] -= 1

        return True