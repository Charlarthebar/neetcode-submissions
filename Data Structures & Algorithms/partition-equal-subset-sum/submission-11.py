class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        goal = total // 2
        have = set()

        for i in range(len(nums) - 1, -1, -1):
            print(have)
            cur = nums[i]
            if cur == goal:
                return True
            if goal - cur in have:
                print(f' cur: {cur}, have:{have}')
                return True
            for n in list(have):
                have.add(n + cur)
            have.add(cur)
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