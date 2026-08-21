class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        i = 0

        while i < len(nums):

            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
            i += 1

        return list(list(item) for item in res)