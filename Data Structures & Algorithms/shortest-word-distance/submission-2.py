class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1Pos = -1
        word2Pos = -1
        res = len(wordsDict) - 1

        for i, word in enumerate(wordsDict):
            if word == word1:
                word1Pos = i
            elif word == word2:
                word2Pos = i

            if word1Pos != -1 and word2Pos != -1:
                res = min(res, abs(word1Pos - word2Pos))

        return res
            