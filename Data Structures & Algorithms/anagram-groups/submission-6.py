class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charMap = defaultdict(list)

        for word in strs:
            chars = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                chars[index] += 1
            chars = tuple(chars)
            charMap[chars].append(word)

        return list(charMap.values())