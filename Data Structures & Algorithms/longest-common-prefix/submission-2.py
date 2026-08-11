class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res, i = [], 0
        stop = False
        while True:
            if i >= len(strs[0]):
                break
            ch = strs[0][i]
            for word in strs:
                if i >= len(word) or word[i] != ch:
                    stop = True
                    break
            if stop:
                break
            i += 1
        return strs[0][:i]

