class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = defaultdict(int)
        for ch in s1:
            s1count[ch] += 1

        count = defaultdict(int)
        l = 0
        matches = 0
        goal = len(s1count)
        for r in range(len(s2)):
            ch = s2[r]
            count[ch] += 1
            if count[ch] == s1count[ch]:
                matches += 1
            elif count[ch] == s1count[ch] + 1:
                matches -= 1

            if r - l + 1 > len(s1):
                ch = s2[l]
                count[ch] -= 1
                if count[ch] == s1count[ch]:
                    matches += 1
                elif count[ch] == s1count[ch] - 1:
                    matches -= 1
                l += 1
            if matches == goal:
                return True
        return False