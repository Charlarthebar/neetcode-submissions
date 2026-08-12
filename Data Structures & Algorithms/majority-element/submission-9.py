class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = None

        for n in nums:
            if count == 0:
                res = n
            count += 1 if n == res else -1
        return res