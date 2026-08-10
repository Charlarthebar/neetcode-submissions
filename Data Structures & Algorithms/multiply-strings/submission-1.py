class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def mult(n1, n2):
            if len(n2) > len(n1):
                n1, n2 = n2, n1
            res = 0

            if len(n2) > 1:
                for i, n in enumerate(n2):
                    res += mult(n1, n) * (10 ** (len(n2) - i - 1))
            else:
                for i, n in enumerate(n1):
                    res += (ord(n1[i]) - ord('0')) * (ord(n2) - ord('0')) * (10 ** (len(n1) - i - 1))
            return res

        return str(mult(num1, num2))