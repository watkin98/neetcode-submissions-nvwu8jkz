class Solution:
    def climbStairs(self, n: int) -> int:

        def rec(i):
            if i <= 0:
                return i == 0

            return rec(i-2) + rec(i-1)

        return rec(n)