class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s)+1)]


        for i in range(1, len(s)+1):
            word = s[:i]

            if word in wordDict:
                dp[i] = True
                continue
            
            for j, elem in enumerate(dp):
                if elem == True:
                    if word[j:] in wordDict:
                        dp[i] = True
                        break
        return dp[len(s)]
