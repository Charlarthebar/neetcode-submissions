class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        total = 0
        res = 0
        for n in nums:
            total += n
            if total == k:
                res += 1
            if total - k in sums:
                res += sums[total - k]
            sums[total] += 1
        
    
        return res