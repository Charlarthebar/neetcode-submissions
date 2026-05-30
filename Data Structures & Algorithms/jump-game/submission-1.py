class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jleft = 0

        for i in range(len(nums) - 1):
            jleft = max(jleft, nums[i])
            if jleft == 0:
                return False
            jleft -= 1
        return jleft >= 0