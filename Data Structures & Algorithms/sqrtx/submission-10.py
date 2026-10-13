class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = None

        while l <= r:
            m = l + ((r-l) // 2)

            if m*m > x:
                r = m - 1
            else:
                res = m
                l = m + 1

        return res
            