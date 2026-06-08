class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf = [0] * len(nums), [0] * len(nums)

        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            pre[i] = prod
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            suf[i] = prod

        res = []
        for i in range(len(nums)):
            first = pre[i - 1] if i - 1 >= 0 else 1
            second = suf[i + 1] if i + 1 < len(nums) else 1
            res.append(first * second)
        return res