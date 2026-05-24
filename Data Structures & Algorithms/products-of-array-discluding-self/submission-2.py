class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [0] * len(nums) 
        # suffix = [0] * len(nums)
        res = [1] * len(nums)
        running = 1
        for i in range(len(nums)-1):
            res[i+1] = running * nums[i]
            running *= nums[i]
        running = 1
        print(res)
        for i in range(len(nums)-1, 0, -1):
            res[i-1] *= running * nums[i]
            running *= nums[i]
        print(res)
        
        # for i in range(len(nums)):
        #     if i-1 >= 0:
        #         res[i] *= prefix[i-1]
        #     if i+1 <= len(nums)-1:
        #         res[i] *= suffix[i+1]

        return res
        # res = [0] * len(nums)
        # product = 1
        # zerocounter = 0
        # for num in nums:
        #     if num != 0:
        #         product *= num
        #     if num == 0:
        #         zerocounter += 1
        
        # if zerocounter == 1:
        #     for i, num in enumerate(nums):
        #         if num == 0:
        #             res[i] = product
        # elif zerocounter > 1:
        #     return res
        # else:
        #     for i in range(len(nums)):
        #         res[i] = product // nums[i]
        
        # return res