class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        h1 = defaultdict(int)
        h2 = defaultdict(int)
        for ch in s1:
            h1[ch] += 1
        for i in range(len(s1)):
            h2[s2[i]] += 1

        l, r = 0, len(s1)
        while r < len(s2):
            if h1 == h2:
                return True
            h2[s2[l]] -= 1
            if h2[s2[l]] == 0:
                del h2[s2[l]]
            l += 1
            h2[s2[r]] += 1
            r += 1
        return h1 == h2