class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        found = True
        while l < r:
            if s[l] != s[r]:
                s1 = s[:l] + s[l + 1:]
                s2 = s[:r] + s[r + 1:]
                found = False
                break
            else:
                l += 1
                r -= 1
        if found:
            return True
        
        print(s1, s2)
    
        for string in (s1, s2):
            l, r = 0, len(string) - 1
            found = True
            while l < r:
                if string[l] != string[r]:
                    found = False
                    break
                else:
                    l += 1
                    r -= 1
            if found:
                return True
        return False