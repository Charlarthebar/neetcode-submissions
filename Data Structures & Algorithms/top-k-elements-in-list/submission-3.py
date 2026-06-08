class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums) + 1)]
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for num, freq in dic.items():
            freqs[freq].append(num)
        
        res = []
        i = len(nums)
        while k != 0:
            for elem in freqs[i]:
                if k == 0:
                    return res
                res.append(elem)
                k -= 1
            i -= 1
        return res
