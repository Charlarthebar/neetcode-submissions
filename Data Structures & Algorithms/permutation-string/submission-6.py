class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = [0] * 26
        for ch in s1:
            s1count[ord(ch) - ord('a')] += 1
        s1count = tuple(s1count)

        count = [0] * 26
        l = 0
        for r in range(len(s2)):
            count[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 > len(s1):
                count[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if tuple(count) == s1count:
                return True
        return False