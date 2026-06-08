class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res = res + strs[i]
            if i == len(strs) - 1:
                continue
            res = res + "'''"
        if res == "" and len(strs) != 1:
            return "None"
        return res 

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        return s.split("'''")