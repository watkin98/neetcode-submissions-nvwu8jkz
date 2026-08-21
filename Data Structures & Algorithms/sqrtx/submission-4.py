class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            m = l + ((r-l) // 2)
            res = m * m

            if res > x:
                r = m - 1
            else:
                while (m+1) * (m+1) <= x:
                    m += 1
                return m