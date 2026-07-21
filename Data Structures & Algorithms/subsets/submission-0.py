class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def helper(numbers):
            if not numbers:
                return [[]]
            first, rest = numbers[0], helper(numbers[1:])
            for i in range(len(rest)):
                l = rest[i]
                rest.append([first] + l)
            return rest
        return helper(nums)