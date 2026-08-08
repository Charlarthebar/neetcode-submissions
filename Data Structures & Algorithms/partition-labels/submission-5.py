class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chToI = {}
        for i, c in enumerate(s):
            if c not in chToI:
                chToI[c] = [i]
            else:
                chToI[c].append(i)

        print(chToI)
        res = []
        i = 0
        while i < len(s):
            ch = s[i]
            nxt = chToI[ch][-1]
            j = i
            while j < nxt + 1:
                if s[j] != ch:
                    nxt = max(nxt, chToI[s[j]][-1])
                j += 1
            print(nxt, i)
            # print(chToI[ch][-1])
            res.append(nxt - i + 1)
            i = nxt + 1
        return res