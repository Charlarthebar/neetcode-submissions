class Solution:
    def climbStairs(self, n: int) -> int:
        second, last = 1, 1
        for i in range(n - 1):
            temp = last
            last = second + last
            second = temp
        return last