class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        p1 = s[i]
        p2 = s[j]

        while i <= j:
            p1 = s[i]
            p2 = s[j]
            if not p1.isalnum():
                i += 1
                continue
            if not p2.isalnum():
                j -= 1
                continue
            if p1.lower() == p2.lower():
                i += 1
                j -= 1
            else:
                return False
        return True