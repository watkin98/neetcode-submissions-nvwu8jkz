class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create character map to store the number of occurances of a character in a given string
        # and iterate through the rest of the strings to build a list containing matching 
        # anagrams

        res = []
        anagram_groups = {}

        for string in strs:
            char_tally = [0] * 26
            for char in string:
                char_tally[ord(char) - ord('a')] += 1

            c_tuple = tuple(char_tally)

            if c_tuple in anagram_groups:
                anagram_groups[c_tuple].append(string)
            else:
                anagram_groups[c_tuple] = [string]

        #print(f"anagram_groups: {anagram_groups.values()}")
        return list(anagram_groups.values())

