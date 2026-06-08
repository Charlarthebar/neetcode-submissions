class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqsToWords = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            s = tuple(count)
            freqsToWords[s].append(word)
        return list(freqsToWords.values())
    
