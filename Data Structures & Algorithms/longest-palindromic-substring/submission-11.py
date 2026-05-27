class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal = ""
        length = 0

        def find_palindromes(p1, p2):
            nonlocal pal, length
            while p1 >= 0 and p2 <= len(s) - 1 and s[p1] == s[p2]:
                if p2 - p1 + 1 > length:
                    pal = s[p1:p2 + 1]
                    length = p2 - p1 + 1
                p1 -= 1
                p2 += 1

        for i in range(len(s)):
            find_palindromes(i, i)
            find_palindromes(i, i + 1)
        return pal