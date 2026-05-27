class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def maximize(houses):
            first, second = 0, 0
            for house in houses:
                temp = second
                second = max(house + first, second)
                first = temp
            return second
        return max(nums[0] + maximize(nums[2:-1]), maximize(nums[1:]))
        