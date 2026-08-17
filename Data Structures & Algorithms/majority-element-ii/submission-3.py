class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hmap = defaultdict(int)

        for n in nums:
            hmap[n] += 1
            if len(hmap) <= 2:
                continue
            
            newhmap = defaultdict(int)
            for n, count in hmap.items():
                if count > 1:
                    newhmap[n] = count - 1
            hmap = newhmap
        
        res = []
        for n in hmap:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res
        