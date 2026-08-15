class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in nums:
                length = 1
                n = num + 1
                while n in nums:
                    length += 1
                    n += 1
                res = max(res, length)
        return res