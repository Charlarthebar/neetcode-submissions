class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        target = len(nums) // 2 if len(nums) % 2 == 0 else len(nums) // 2 + 1

        for n in nums:
            counts[n] += 1
            if counts[n] == target:
                return n