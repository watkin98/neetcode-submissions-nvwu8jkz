class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        maxSubset = 0

        for r in range(len(s)):
            char = s[r]
            if char not in seen:
                seen.add(char)
                print("if")
                print(seen)
                maxSubset = max(maxSubset, len(seen))
            else:
                print("else")
                while char in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[l])
                seen.add(s[r])
                print(seen)

        return maxSubset

