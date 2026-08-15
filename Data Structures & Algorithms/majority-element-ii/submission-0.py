class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums) // 3 + 1
        counts = defaultdict(int)
        res = []
        for n in nums:
            counts[n] += 1
            if counts[n] == target:
                res.append(n)
        return res