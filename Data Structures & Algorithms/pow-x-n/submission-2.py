class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(n) -> float:
            if x == 0:
                return 0
            if n == 0:
                return 1.0

            res = helper(n // 2)
            res = res * res
            return x * res if n % 2 else res

        res = helper(abs(n))
        return res if n > 0 else 1/res