class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) > 1:
            s1, s2 = -heapq.heappop(heap), -heapq.heappop(heap)
            if s1 == s2:
                continue
            elif s1 < s2:
                heapq.heappush(heap, -(s2 - s1))
            elif s2 < s1:
                heapq.heappush(heap, -(s1 - s2))
        return -heap[0] if heap else 0
