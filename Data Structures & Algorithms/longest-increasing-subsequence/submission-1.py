class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxToCounts = {num: -1 for num in nums}
        res = 1

        for num in nums:
            for m, count in maxToCounts.items():
                if (m != num and # make sure not itself
                count != -1 and # make sure have passed through it
                num >= m and # make sure new number is greater
                maxToCounts[m] + 1 > maxToCounts[num]): # number starting at sequence n is greater than current length
                    print(num, m, count)
                    maxToCounts[num] = maxToCounts[m] + 1
                    res = max(res, maxToCounts[num])
            if maxToCounts[num] == -1:
                maxToCounts[num] = 1 
        print(maxToCounts)
        return res
