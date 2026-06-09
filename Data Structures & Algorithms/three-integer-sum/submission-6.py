class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i - 1] == num:
                continue
            
            while r > l:
                total = num + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], num])
                    r -= 1
                    l += 1
                    # while l < r and nums[l - 1] == nums[l]:
                    #     l += 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1
        return res
