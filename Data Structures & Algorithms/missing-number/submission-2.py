class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total = total ^ num
        for i in range(len(nums)+1):
            total = total ^ i
        return total