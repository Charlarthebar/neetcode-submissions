class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums) + 1)]
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        
        for n, count in counts.items():
            freqs[count].append(n)
        
        res = []
        used = 0
        for i in range(len(nums), -1, -1):
            for n in freqs[i]:
                res.append(n)
                used += 1
                if used == k:
                    return res