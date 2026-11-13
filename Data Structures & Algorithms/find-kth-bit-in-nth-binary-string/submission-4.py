class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = ""

        def helper(n):
            nonlocal s
            if n == 0:
                return '0'
            # if len(s) >= k:
            #     return '0'

            substr = helper(n-1)

            rev = []
            for c in substr:
                if c == '1':
                    rev.append('0')
                else:
                    rev.append('1')

            return substr + '1' + ''.join(rev[::-1])

        return helper(n)[k-1]
