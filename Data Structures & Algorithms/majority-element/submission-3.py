class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = None

        for n in nums:
            if n == res:
                count += 1
            else:
                if count == 0:
                    count += 1
                    res = n
                else:
                    count -= 1
        return res