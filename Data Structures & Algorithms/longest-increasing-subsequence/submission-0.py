class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxToCounts = {num: -1 for num in nums}
        res = 1

        for num in nums:
            for m, count in maxToCounts.items():
                if m != num and count != -1 and num >= m and maxToCounts[m] + 1 > maxToCounts[num]:
                    print(num, m, count)
                    maxToCounts[num] = maxToCounts[m] + 1
                    res = max(res, maxToCounts[num])
            if maxToCounts[num] == -1:
                maxToCounts[num] = 1 
        print(maxToCounts)
        return res
