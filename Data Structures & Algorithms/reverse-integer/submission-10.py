class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        res = 0
        while x >= 10:
            res = res * 10 + (x % 10)
            x //= 10
        
        print(res)
        if sign == 1:
            if res > (2 ** 31 - 1) // 10:
                return 0
            elif res < (2 ** 31 - 1) // 10:
                res = res * 10 + (x % 10)
            else:
                if x > (2 ** 31 - 1) % 10:
                    return 0
                else:
                    res = res * 10 + (x % 10)
        else:
            if res > (2 ** 31) // 10:
                return 0
            elif res < (2 ** 31) // 10:
                res = res * 10 + (x % 10)
            else:
                if x > (2 ** 31) % 10:
                    return 0
                else:
                    res = res * 10 + (x % 10)
        res *= sign

        return res