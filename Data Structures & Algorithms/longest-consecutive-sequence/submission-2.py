class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 1
        if not nums:
            return 0
        for num in nums:
            i = num + 1
            if num - 1 not in s:   # if start of sequence
                cur = 1 
                while i in s:
                    cur += 1
                    i += 1
                longest = max(longest, cur)
        return longest