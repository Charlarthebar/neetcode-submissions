class MedianFinder:

    def __init__(self):
        self.minHeap = []
        heapq.heapify(self.minHeap)
        self.maxHeap = []    
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if not self.minHeap or num < self.minHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if len(self.maxHeap) - len(self.minHeap) >= 2:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        
        if len(self.minHeap) - len(self.maxHeap) >= 2:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)

    def findMedian(self) -> float:
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            return (self.minHeap[0] + -self.maxHeap[0]) / 2
        else:
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            else:
                return -self.maxHeap[0]