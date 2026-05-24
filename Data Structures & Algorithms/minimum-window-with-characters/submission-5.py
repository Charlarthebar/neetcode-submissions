class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0

        ans = (float("inf"), 0, 0)
        count_t = defaultdict(int)
        curcount = defaultdict(int)
        charsmet = 0

        if len(t) > len(s):
            return ""
        for ch in t:
            count_t[ch] += 1
        
        for r in range(len(s)):
            if s[r] in count_t:
                curcount[s[r]] += 1
                if curcount[s[r]] == count_t[s[r]]:
                    charsmet += 1
            while charsmet == len(count_t):
                if r-l+1 < ans[0]:
                    ans = (r-l+1, l, r)
                
                if s[l] in count_t:
                    curcount[s[l]] -= 1
                    if curcount[s[l]] < count_t[s[l]]:
                        charsmet -= 1
                l += 1

        if ans[0] == float("inf"):
            return ""
        return s[ans[1]:ans[2]+1]



        # create freq dict of t

        # increment r until you reach the end of the strong s
        #     if current character is in count
        #         curcount[s[r]] += 1
        #         if curcount[s[r]] is equal to count[s[r]]
        #             charsmet += 1
        #     while charsmet is equal to len(count)
        #     while the string from index l to index r is a string that contains all the letters of t
        #         if len(current string) < len(ans):
        #             set ans to this string from l to r
        #         increment l
            