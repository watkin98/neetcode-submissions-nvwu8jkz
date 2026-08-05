class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_counts = defaultdict(list)

        for word in strs:
            chars = [0] * 27
            for char in word:
                index = ord(char) - ord('a')
                chars[index] += 1
            
            charsTuple = tuple(chars)
            letter_counts[charsTuple].append(word)

        return list(letter_counts.values())