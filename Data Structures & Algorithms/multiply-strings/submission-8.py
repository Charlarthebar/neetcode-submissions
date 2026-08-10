class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                prod = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                res[i + j] += prod

        for i in range(len(res)):
            if res[i] >= 10:
                val, carry = res[i] % 10, res[i] // 10
                res[i] = val
                res[i + 1] += carry

        while res and res[-1] == 0:
            res.pop()
        return "".join(map(str, res[::-1]))