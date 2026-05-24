class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        changes = 0
        l = 0
        freqs = defaultdict(int)
        mostFreq = 0
        maxLength = 0
        for r, ch in enumerate(s):
            freqs[ch] += 1
            mostFreq = max(mostFreq, freqs[ch])
            while (r - l + 1) - mostFreq > k:
                freqs[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, (r - l + 1))
        return maxLength