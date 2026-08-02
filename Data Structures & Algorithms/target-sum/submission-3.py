class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        t = sum(nums)
        if t < target:
            return 0
        dp = [0] * (2 * t + 1)
        m = t // 2
        dp[t + target] = 1

        for i in range(len(nums) - 1, -1, -1):
            newdp = dp[:]
            for num in range(2 * t, -1, -1):
                n1 = dp[num + nums[i]] if num + nums[i] < len(dp) else 0
                n2 = dp[num - nums[i]] if num - nums[i] >= 0 else 0
                newdp[num] = n1 + n2
            dp = newdp
            print(dp)
        return dp[t]