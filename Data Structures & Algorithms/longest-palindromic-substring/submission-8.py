class Solution:
    def longestPalindrome(self, s: str) -> str:
        p1, p2 = 0, len(s) - 1
        palindrome = (s[0], 0)
        def is_palindrome(start, end):
            possible = s[start:end + 1]
            while start < end:
                if s[start] != s[end]:
                    return ""
                start += 1
                end -= 1
            return possible
        
        for i in range(len(s)):
            p1, p2 = i, len(s) - 1
            if p2 - p1 + 1 < palindrome[1]:
                continue
            while p1 < p2:
                char1, char2 = s[p1], s[p2]
                if char1 == char2:
                    res = is_palindrome(p1, p2)
                    if len(res) > palindrome[1]:
                        palindrome = (res, len(res))
                        break
                p2 -= 1
        return palindrome[0]