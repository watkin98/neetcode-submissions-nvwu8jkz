class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def helper(n):
            if n == 0:
                return '0'

            s = helper(n-1)
            if len(s) >= k:
                return s

            rev = []
            for c in s:
                if c == '1':
                    rev.append('0')
                else:
                    rev.append('1')

            return s + '1' + ''.join(rev)[::-1]

        res = helper(n)
        return res[k-1]
