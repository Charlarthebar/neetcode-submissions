class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        for l in range(len(s2) - len(s1) + 1):
            
            r = l + len(s1)
            print(s2[l:r+1])
            if Counter(s1) == Counter(s2[l:r]):
                return True
        return False