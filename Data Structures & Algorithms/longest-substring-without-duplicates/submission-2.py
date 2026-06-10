class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        l, r = 0, 0
        res = 0

        while r < len(s):
            if s[r] not in cur:
                cur.add(s[r])
                r += 1
                res = max(res, len(cur))
                continue
            print(l, s[l])
            print(r, s[r])
            while s[l] != s[r]:
                # print(cur)
                # print(l, s[l])
                # print(r, s[r])
                
                cur.remove(s[l])
                l += 1
            print(l, s[l])
            print(r, s[r])
            l += 1
            r += 1
        return res
            
            