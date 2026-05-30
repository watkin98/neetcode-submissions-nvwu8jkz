class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chrTallies = defaultdict(int)

        for char in s:
            chrTallies[char] += 1

        for char in t:
            if char not in chrTallies:
                return False
            
            chrTallies[char] -= 1

            if chrTallies[char] < 0:
                return False

        return True