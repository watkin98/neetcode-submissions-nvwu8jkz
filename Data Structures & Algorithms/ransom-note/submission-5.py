class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charTracker = defaultdict(int)

        for magChar in magazine: 
            charTracker[magChar] += 1

        for noteChar in ransomNote:
            if charTracker[noteChar] == 0:
                return False
            else:
                charTracker[noteChar] -= 1

        return True