class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        counter = 0
        counterFlag = False

        for word in wordsDict:
            if counterFlag is True:
                counter += 1
            
            if counterFlag is True and (word == word1 or word == word2):
                break

            if (word == word1 or word == word2) and counterFlag is False:
                counterFlag = True

        return counter