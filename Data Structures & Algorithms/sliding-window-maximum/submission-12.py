class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        print(heap)
        
        for i in range(len(nums) - k):
            res.append(-heap[0][0])
            while heap and heap[0][1] < i + 1:
                heapq.heappop(heap)
            heapq.heappush(heap, (-nums[i + k], i+k))
            
        res.append(-heap[0][0])
        print(heap)
        return res