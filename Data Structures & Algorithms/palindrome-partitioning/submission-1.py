class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(i, j):
            l, r = i, j
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        def dfs(i, substrings):
            if i == len(s):
                res.append(substrings[:])
                return
            
            for j in range(i + 1, len(s)+1):
                if isPalindrome(i, j-1):
                    substrings.append(s[i:j])
                    dfs(j, substrings)
                    substrings.pop()

        dfs(0, [])
        return res