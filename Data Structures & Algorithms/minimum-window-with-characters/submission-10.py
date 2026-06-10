class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tcount = defaultdict(int)
        for ch in t:
            tcount[ch] += 1
        scount = defaultdict(int)

        res = 0, float('inf')
        have, need = 0, len(tcount)
        l = 0
        for r in range(len(s)):
            scount[s[r]] += 1
            if scount[s[r]] == tcount[s[r]]:
                have += 1
            while have == need:
                if r - l < res[1] - res[0]:
                    res = l, r
                scount[s[l]] -= 1
                if scount[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1
        return "" if res[1] == float('inf') else s[res[0]: res[1] + 1]
            

            