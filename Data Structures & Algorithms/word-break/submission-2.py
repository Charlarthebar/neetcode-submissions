class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        possibleWords = set()
        wordDict = set(wordDict)

        for i in range(len(s)):
            word = s[:i+1]
            if word in wordDict:
                possibleWords.add(word)
                continue
            
            for w in list(possibleWords):

                if word[len(w):] in wordDict:
                    possibleWords.add(word)
                    continue

        return s in possibleWords