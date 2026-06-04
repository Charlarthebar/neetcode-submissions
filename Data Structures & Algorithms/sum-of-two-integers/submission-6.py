class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0

        for i in range(32):
            abit = a & 1
            bbit = b & 1
            print(abit, bbit)
            val = 0
            if carry and abit and bbit:
                val = 1
                carry = 1
            elif (carry and abit) or (carry and bbit) or (abit and bbit):
                val = 0
                carry = 1
            elif carry or abit or bbit:
                val = 1
                carry = 0
            else:
                val = 0
                carry = 0
            
            res |= (val << i)
            a >>= 1
            b >>= 1
            print(bin(res))
        if res & (1 << 31):
            return res - (1 << 32)
        return res
