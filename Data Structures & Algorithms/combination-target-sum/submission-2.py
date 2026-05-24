class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(nums, target, cur_nums):
            if not nums or target < 0:
                return None
            if target == 0:
                res.append(cur_nums.copy())
                return
            first, rest = nums[0], nums[1:]

            # try possibility including first number 
            cur_nums.append(first)
            possible = helper(nums, target-first, cur_nums)
            cur_nums.pop()
            # try possibility without first number
            helper(rest, target, cur_nums)
        helper(nums, target, [])
        return res

        # def helper(start, target, cur_nums):
        #     if target < 0:
        #         return None
        #     elif target == 0:
        #         return cur_nums[:]
            
        #     for i in range(start, len(nums)):
        #         cur_nums.append(nums[i])
        #         possible_sol = helper(i, target - nums[i], cur_nums)
        #         if possible_sol:
        #             res.append(possible_sol)
        #         cur_nums.pop()
        #     return None
        # helper(0, target, [])
        # return res