class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n

        curProduct = x
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= curProduct

            curProduct *= curProduct
            n >>= 1

        return res
