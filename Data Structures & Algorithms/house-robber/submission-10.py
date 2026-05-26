class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        money = [0] * len(nums)
        money[0], money[1] = nums[0], max(nums[0], nums[1])
        print(money)
        for i in range(2, len(nums)):
            money[i] = max(nums[i] + money[i - 2], money[i - 1])
        print(money)
        return money[-1]