class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for num in range(len(nums) + 1):
            total += num
        for num in nums:
            total -= num
        return total