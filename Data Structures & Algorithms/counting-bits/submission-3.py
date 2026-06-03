class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0 for _ in range(n + 1)]
        for i in range(n + 1):
            if i == 0:
                res[i] = 0
                continue
            if i == 1:
                res[i] = 1
                continue
            if i == 2:
                res[i] = 1
                continue
            if i == 3:
                res[i] = 2
                continue
            shift = 2 ** (i.bit_length() - 1)
            res[i] = res[i - shift] + 1
        return res