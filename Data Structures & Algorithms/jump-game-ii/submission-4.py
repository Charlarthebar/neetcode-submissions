class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        goal = len(nums) - 1
        dp[goal] = 0

        for i in range(len(nums) - 2, -1, -1):
            d = float('inf')
            for j in range(i + 1, i + nums[i] + 1):
                print(i, j)
                if j > goal:
                    break
                if j == goal:
                    d = 1
                    break
                d = min(d, 1 + dp[j])
            dp[i] = d
        print(dp)
        return dp[0]