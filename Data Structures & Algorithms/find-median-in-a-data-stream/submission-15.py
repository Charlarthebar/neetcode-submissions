class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        if self.minHeap and num > self.minHeap[0]:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)

        if len(self.maxHeap) - 1 > len(self.minHeap):
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        if len(self.maxHeap) < len(self.minHeap) - 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
        
    def findMedian(self) -> float:
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        else:
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            else:
                return self.maxHeap[0] * -1
        
        