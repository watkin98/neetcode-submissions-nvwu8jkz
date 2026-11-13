class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def helper(n):
            if n == 0:
                return '0'

            substr = helper(n-1)
            if len(substr) >= k:
                return substr

            rev = []
            for c in substr:
                if c == '1':
                    rev.append('0')
                else:
                    rev.append('1')

            return substr + '1' + ''.join(rev[::-1])

        return helper(n)[k-1]
