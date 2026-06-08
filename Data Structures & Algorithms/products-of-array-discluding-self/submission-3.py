class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf = [], []

        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            pre.append(prod)
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            suf.append(prod)

        res = []
        for i in range(len(nums)):
            first = pre[i - 1] if i - 1 >= 0 else 1
            second = suf[len(nums) - 2 - i] if len(nums) - 2 - i >= 0 else 1
            res.append(first * second)
        return res