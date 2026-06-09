class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            
            while r > l:
                total = num + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.add((nums[l], nums[r], num))
                    r -= 1
                    l += 1
        res = list(res)
        for i in range(len(res)):
            res[i] = list(res[i])
        return res
