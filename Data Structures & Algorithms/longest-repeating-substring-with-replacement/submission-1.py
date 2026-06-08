class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        maxLen = 0

        for char in charSet:
            l = count = 0
            for r in range(len(s)):
                if char == s[r]:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1
                maxLen = max(maxLen, r - l + 1)

        return maxLen