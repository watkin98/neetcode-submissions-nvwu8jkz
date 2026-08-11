class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, replacements = 0, 1, k
        maxLen = 1
        currLen = 1

        while r < len(s):
            print(f"{s[r]} == {s[l]}")
            if s[r] == s[l]:
                r += 1
                currLen += 1
                maxLen = max(maxLen, currLen)
                print(f"1 maxLen: {maxLen}")
                continue
            
            if replacements > 0:
                r += 1
                replacements -= 1
                currLen += 1
                maxLen = max(maxLen, currLen)
                print(f"2 maxLen: {maxLen}")
            else:
                while s[l] == s[l + 1]:
                    l += 1
                l += 1
                r = l + 1
                replacements += 1
                currLen = 1

        return maxLen
