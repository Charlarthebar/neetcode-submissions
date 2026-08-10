class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / (self.myPow(x, -n))
        if n == 0:
            return 1
        if n == 2:
            return x * x

        extra = 1
        if n % 2 == 1:
            extra = x

        return self.myPow(self.myPow(x, n // 2), 2) * extra