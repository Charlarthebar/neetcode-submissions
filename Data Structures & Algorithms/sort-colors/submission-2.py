class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        while r < len(nums):
            if nums[l] == 0:
                l += 1
                r = l
            elif nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                r += 1
            else:
                r += 1
        print(nums)
        
        l, r = len(nums) - 1, len(nums) - 1
        while l >= 0:
            if nums[r] == 2:
                r -= 1
                l = r
            elif nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                l -= 1
            else:
                l -= 1
        print(nums)

