class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if not n:
                print(bin(res))
                return res
            # rightBit = n % 2
            res |= (((n >> i) % 2) << (31 - i))
            # n >>= 1

        
        
        return res