class PrefixTree:

    def __init__(self):
        self.hmp = {}

    def insert(self, word: str) -> None:
        m = self.hmp
        for i in range(len(word)):
            if word[i] not in m:
                m[word[i]] = {}
            m = m[word[i]]     
        m['*'] = {}

    def search(self, word: str) -> bool:
        m = self.hmp
        for i in range(len(word)):
            if word[i] not in m:
                return False
            m = m[word[i]]

        return '*' in m

    def startsWith(self, prefix: str) -> bool:
        m = self.hmp
        for i in range(len(prefix)):
            if prefix[i] not in m:
                return False
            m = m[prefix[i]]
        return True
        