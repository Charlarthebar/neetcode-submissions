class Solution:
    def isHappy(self, n: int) -> bool:
        fast = n
        slow = n

        def happy(n):
            res = 0
            while n:
                res += (n % 10) ** 2
                n = n // 10
            return res
        
        while fast and slow:
            
            slow = happy(slow)
            fast = happy(happy(fast))
            if fast == 1 or slow == 1:
                return True
            if slow == fast:
                return False
        return True