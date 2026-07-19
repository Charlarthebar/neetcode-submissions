class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            heap.append((math.sqrt(x**2 + y**2), point))
        heapq.heapify(heap)
        
        res = []
        while len(res) < k:
            dist, point = heapq.heappop(heap)
            res.append(point)
        return res

