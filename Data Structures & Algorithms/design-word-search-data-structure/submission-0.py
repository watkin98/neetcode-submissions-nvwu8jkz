class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['*'] = {}

    def search(self, word: str) -> bool:
        curr = self.trie
        for char in word:
            if char == '.':
                new_curr = {}
                for key in curr:
                    temp = curr[key]
                    for key1 in temp:
                        new_curr[key1] = temp[key1]
                curr = new_curr
            elif char not in curr:
                return False
            else:
                curr = curr[char]

        return '*' in curr
