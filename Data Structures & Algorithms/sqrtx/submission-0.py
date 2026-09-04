class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x - 1

        while l <= r:
            mid = l + (r-l) // 2
            sqr = mid * mid

            if sqr > x:
                r = mid - 1
            elif sqr < x:
                l = mid + 1
            else:
                return mid

        return min(r, l)