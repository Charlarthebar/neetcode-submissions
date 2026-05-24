class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # (num : frequency)
        l = [[] for _ in range(len(nums) + 1)] # index is frequency, [num]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key in freq:
            l[freq[key]].append(key)
        
        print(freq)
        print(l)

        count = 0
        output = []
        for i in range(len(nums), -1, -1):
            if l[i]:
                output += l[i]
                count += len(l[i])
            if count == k:
                return output