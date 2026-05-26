class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        money = [-1] * len(nums)

        def helper(i):
            if i < 2:
                # print(nums[i])
                money[i] = nums[i]
                return max(nums[i], nums[i - 1]) if i == 1 else nums[i]
            if money[i] != -1:
                return money[i]
            res = max(nums[i] + helper(i - 2), helper(i - 1))
            money[i] = res
            return res

        return helper(len(nums) - 1)
        # money[-1] = nums[-1]
        # money[-2] = nums[-2]
        # for i in range(len(nums)-3, -1, -1):
        #     print(money[i], money[i + 2])
        #     money[i] = nums[i] + money[i + 2]
            
        # print(money)
        # return max(money)