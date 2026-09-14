class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_maps = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                freq[index] += 1
            key = tuple(freq)
            freq_maps[key].append(s)

        return list(freq_maps.values())