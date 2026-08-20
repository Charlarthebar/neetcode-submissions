class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            n = nums[i]
            if n == i + 1:
                i += 1
            elif 1 <= n <= len(nums) and nums[n - 1] != n:
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
            else:
                i += 1

        for i, n in enumerate(nums):
            if n != i + 1:
                return i + 1
        return len(nums) + 1