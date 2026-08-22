class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = defaultdict(int)
        res = 0
        maxFreq = 0

        for r in range(len(s)):
            ch = s[r]
            counts[ch] += 1
            maxFreq = max(maxFreq, counts[ch])
            # if ch != maxChar:
            #     replace += 1
            #     if counts[ch] > counts[maxChar]:
            #         maxChar = ch
            replace = r - l + 1 - maxFreq
                    # print(r, maxChar, replace)
            # print(r)
            while replace > k:
                # print("here")
                counts[s[l]] -= 1
                l += 1
                maxFreq = max(counts.values())
                replace = r - l + 1 - maxFreq
            # print(res, r - l + 1)
            res = max(res, r - l + 1)
        return res
            