class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteChar = 0
        
        for magChar in magazine:
            if magChar == ransomNote[noteChar]:
                noteChar += 1

            if noteChar == len(ransomNote):
                return True

        return False
