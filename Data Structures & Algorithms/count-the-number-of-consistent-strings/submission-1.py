class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0

        for word in words:
            isAllowed = True
            for char in word:
                if char not in allowed:
                    isAllowed = False
                    break
            if isAllowed:
                res += 1

        return res