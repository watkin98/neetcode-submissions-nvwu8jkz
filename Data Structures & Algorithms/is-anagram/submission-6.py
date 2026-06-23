class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount = defaultdict(int)

        for char in s:
            charCount[char] += 1

        for char in t:
            if charCount[char] == 0:
                return False
            charCount[char] -= 1

        for char in charCount:
            if charCount[char] > 0:
                return False

        return True