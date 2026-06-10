class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tcount = defaultdict(int)
        for ch in t:
            tcount[ch] += 1
        scount = defaultdict(int)

        res = "", float('inf')
        l = 0
        for r in range(len(s)):
            scount[s[r]] += 1
            valid = True
            while valid:
                for c in tcount:
                    if scount[c] < tcount[c]:
                        valid = False
                        break
                if valid:
                    if (r - l + 1) < res[1]:
                        res = s[l:r+1], r-l+1
                    scount[s[l]] -= 1
                    l += 1
        return res[0]
            

            