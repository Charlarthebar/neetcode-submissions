class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(string):
            l, r = 0, len(string) - 1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        def dfs(i, substrings):
            print(i, substrings)
            if i == len(s):
                res.append(substrings[:])
                return
            
            for j in range(i + 1, len(s)+1):
                possible = s[i : j]
                if isPalindrome(possible):
                    substrings.append(possible)
                    dfs(j, substrings)
                    substrings.pop()
            return
        dfs(0, [])
        return res