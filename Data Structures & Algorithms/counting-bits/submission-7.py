class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0 for _ in range(n + 1)]
        for i in range(n + 1):
            if i == 0:
                res[i] = 0
                continue

            shift = 1 << (i.bit_length() - 1)
            res[i] = res[i - shift] + 1
        return res