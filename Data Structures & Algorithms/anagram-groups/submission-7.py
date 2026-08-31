class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            frqCnt = [0] * 26
            for c in s:
                key = ord(c) - ord('a')
                frqCnt[key] += 1

            key = tuple(frqCnt)
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]

        return list(anagrams.values())