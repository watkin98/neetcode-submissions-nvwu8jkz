class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        minLen = len(wordsDict)
        wordSet = set([word1, word2])
        l, r = 0, 1
        while wordsDict[l] != word1 and wordsDict[l] != word2:
            l += 1
            r += 1

        while r < len(wordsDict):
            if wordsDict[l] != wordsDict[r] and wordsDict[r] in wordSet:
                minLen = min(minLen, r - l)
                l = r
            elif wordsDict[l] == wordsDict[r]:
                l = r
            r += 1

        return minLen