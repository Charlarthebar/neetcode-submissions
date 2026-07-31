class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        goal = total // 2
        have = {0}

        for cur in nums:
            for curSum in list(have):
                newSum = curSum + goal
                if curSum + cur == goal:
                    return True
                
                have.add(curSum + cur)
        return False
        
        # i, j = 0, len(nums) - 1
        # total = sum(nums)
        # goal = total // 2
        # if total % 2 == 1:
        #     return False
        # cur = total
        # print(total // 2)

        # dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        # while j >= 0:
        #     total -= nums[j + 1] if j + 1 < len(nums) else 0
        #     i = 0
        #     while i <= j:
        #         dp[i][j] = cur
        #         if cur == goal:
        #             # for row in dp:
        #             #     print(row)
        #             return True
        #         cur -= nums[i]
        #         i += 1
        #     cur = total - nums[j]
        #     j -= 1
        # for row in dp:
        #     print(row)
        # return False