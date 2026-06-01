class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}

        for string in strs:
            alphabet = [0] * 26
            for char in string:
                num = ord(char) - ord('a')
                alphabet[num] += 1
            
            key = tuple(alphabet)

            if key not in counts:
                counts[key] = [string]
            else:
                counts[key].append(string)

        print(counts.values())
        return list(counts.values())