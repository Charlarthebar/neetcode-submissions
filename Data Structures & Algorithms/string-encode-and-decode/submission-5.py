class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f'{len(s)}#{s}')
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0

        while l < len(s):
            while s[r] != "#":
                r += 1
            
            strLen = int(s[l:r])
            res.append(s[r + 1: r + 1 + strLen])
            l = r + 1 + strLen
            r = l
        return res