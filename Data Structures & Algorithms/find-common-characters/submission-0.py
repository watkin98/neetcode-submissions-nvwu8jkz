class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        dictArray = []
        res = []

        for word in words:
            wordDict = defaultdict(int)
            for char in word:
                wordDict[char] += 1
            dictArray.append(wordDict)

        firstWord = words[0]
        dictArray = dictArray[1:]
        print(dictArray)
        for char in firstWord:
            notFound = True
            for dictionary in dictArray:
                if dictionary[char] == 0:
                    notFound = False
                    break
                dictionary[char] -= 1
            if notFound:
                res.append(char)

        return res