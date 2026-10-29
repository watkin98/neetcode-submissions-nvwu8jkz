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
        def dfs(i, node):
            if i == len(word):
                return '*' in node

            char = word[i]
            if char == '.':
                for key in node:
                    if dfs(i + 1, node[key]):
                        return True
                return False
            else:
                if char in node:
                    return dfs(i + 1, node[char])
                return False
        return dfs(0, self.trie)