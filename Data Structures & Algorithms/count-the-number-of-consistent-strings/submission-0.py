class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        charSet = set()

        for char in allowed:
            charSet.add(char)

        for word in words:
            isConsistent = True
            
            for char in word:
                if char not in charSet:
                    isConsistent = False
                    break

            if isConsistent:
                res += 1

        return res
