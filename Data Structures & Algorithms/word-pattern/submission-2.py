class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping1 = defaultdict(str)
        mapping2 = defaultdict(str)
        words = s.split(' ')
        if len(pattern) > len(words):
            print(len(s))
            print(len(words))
            return False
        
        for i, char in enumerate(pattern):
            if mapping1[char] == '':
                mapping1[char] = words[i]
            elif mapping1[char] != words[i]:
                return False

        for i, word in enumerate(words):
            if mapping2[word] == '':
                mapping2[word] = pattern[i]
            elif i >= len(pattern) or mapping2[word] != pattern[i]:
                return False

        return True