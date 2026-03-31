class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newStrsList = []
        groupedAnagrams = []

        for string in strs:
            strsMap = {}

            for char in string:
                if char in strsMap:
                    strsMap[char] += 1
                else:
                    strsMap[char] = 1
            
            wordPair = (string, strsMap)
            newStrsList.append(wordPair)

        while len(newStrsList) != 0:
            wordPair = newStrsList.pop(0)
            word = wordPair[0]
            wordMap = wordPair[1]
            words = [word]

            for item in newStrsList:
                if item[1] == wordMap:
                    words.append(item[0])

            groupedAnagrams.append(words)

            for item in words:
                for pair in newStrsList:
                    if item == pair[0]:
                        newStrsList.remove(pair)

        return groupedAnagrams

