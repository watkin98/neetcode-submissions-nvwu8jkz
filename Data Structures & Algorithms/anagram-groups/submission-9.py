class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            char_map = [0] * 26
            for c in s:
                i = ord('a') - ord(c)
                char_map[i] += 1
            
            char_map = tuple(char_map)
            if char_map in anagrams:
                anagrams[char_map].append(s)
            else:
                anagrams[char_map] = [s]

        return list(anagrams.values())