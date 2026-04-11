class Solution:
    def isPalindrome(self, s: str) -> bool:
        lft, rgt = 0, len(s) - 1

        while lft < rgt:

            while s[lft].isalnum() is not True and lft < rgt:
                lft += 1
            while s[rgt].isalnum() is not True and lft < rgt:
                rgt -= 1

            if s[lft].lower() != s[rgt].lower():
                return False

            lft += 1
            rgt -= 1

        return True
