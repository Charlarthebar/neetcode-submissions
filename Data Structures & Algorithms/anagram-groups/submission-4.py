class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqsToWords = {}
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            s = tuple(count)
            if s in freqsToWords:
                freqsToWords[s].append(word)
            else:
                freqsToWords[s] = [word]
        return list(freqsToWords.values())
    
