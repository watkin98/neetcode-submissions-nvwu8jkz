class Solution:
    def isPalindrome(self, s: str) -> bool:
        # recreate the string with only alphanumeric characters
        s_lower = s.lower()
        #print(f"s lower: {s_lower}")
        new_s = "".join([char for char in s_lower if char.isalnum()])
        #print(f"new_s  : {new_s}")
        # create 2 pointers to traverse the new string, one from
        # the front and another from the back
        n = len(new_s)
        lft_ptr = 0
        rgt_ptr = n - 1

        # loop through the new string from each end until the 
        # pointers meet in the middle
            # if at any point the chars pointed to !=, return false
        while lft_ptr < rgt_ptr:
            if new_s[lft_ptr] != new_s[rgt_ptr]:
                return False

            lft_ptr += 1
            rgt_ptr -= 1
        # loop completed without false exit, return true
        return True

