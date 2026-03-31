class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #strsMap = {}
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

        #print(1)
        #print(newStrsList)
        while len(newStrsList) != 0:
            print(f"Beginning newStrsList: {newStrsList}")
            print(f"Beginning groupedAnagrams: {groupedAnagrams}")
            wordPair = newStrsList.pop(0)
            word = wordPair[0]
            wordMap = wordPair[1]
            words = [word]
            #print(word)
            #print(wordMap)
            #if [word] not in groupedAnagrams:
            #    groupedAnagrams.append([word])
            #    newStrsList.remove(wordPair)
            #else:
            #    for 
            for item in newStrsList:
                if item[1] == wordMap:
                    words.append(item[0])

            groupedAnagrams.append(words)

            for item in words:
                for pair in newStrsList:
                    if item == pair[0]:
                        newStrsList.remove(pair)

            print(f"End newStrsList: {newStrsList}")
            print(f"End groupedAnagrams: {groupedAnagrams}")

        return groupedAnagrams

