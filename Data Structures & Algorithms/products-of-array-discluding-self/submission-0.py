class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        product = 1
        zerocounter = 0
        for num in nums:
            if num != 0:
                product *= num
            if num == 0:
                zerocounter += 1
        
        if zerocounter == 1:
            for i, num in enumerate(nums):
                if num == 0:
                    res[i] = product
        elif zerocounter > 1:
            return res
        else:
            for i in range(len(nums)):
                res[i] = product // nums[i]
        
        return res