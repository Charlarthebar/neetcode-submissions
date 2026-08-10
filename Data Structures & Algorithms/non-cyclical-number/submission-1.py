class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        seen = {n}
        s = 0
        while True:
            # print(s)
            for d in str(n):
                s += int(d) ** 2
            n = s
            s = 0
            if n in seen:
                return False
            if n == 1:
                return True
            seen.add(n)