class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maximum = nums[0]
        minimum = nums[0]
        
        for i in range(1, len(nums)):
            val1, val2, val3 = nums[i], maximum * nums[i], minimum * nums[i]
            maximum = max(val1, val2, val3)
            minimum = min(val1, val2, val3)
            print(nums[i], maximum, minimum)
            print()
            res = max(res, maximum)
        return res