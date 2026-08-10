class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / (self.myPow(x, -n))
        if n == 0:
            return 1

        extra = 1
        if n % 2 == 1:
            extra = x

        return self.myPow(x * x, n // 2) * extra