class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for div in range(31, -1, -1):
            if (2 ** div) <= n:
                n -= (2 ** div)
                count += 1
                print(n)
        return count