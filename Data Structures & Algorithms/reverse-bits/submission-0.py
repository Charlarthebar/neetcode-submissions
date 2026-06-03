class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if not n:
                print(bin(res))
                return res
            rightBit = n % 2
            res |= (rightBit << (31 - i))
            print(bin(n))
            n >>= 1

        
        
        return res