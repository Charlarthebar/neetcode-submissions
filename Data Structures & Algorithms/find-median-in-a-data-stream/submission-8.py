class MedianFinder:

    def __init__(self):
        self.less = []
        self.greater = []
        heapq.heapify(self.less)
        heapq.heapify(self.greater)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.less, -1 * num)
        if len(self.less) - len(self.greater) > 1:
            val = -1 * heapq.heappop(self.less)
            heapq.heappush(self.greater, val)
        if self.greater:
            if self.less[0] * -1 > self.greater[0]:
                val = -1 * heapq.heappop(self.less)
                heapq.heappush(self.greater, val)
        if len(self.greater) > len(self.less):
            val = heapq.heappop(self.greater)
            heapq.heappush(self.less, -val)

    def findMedian(self) -> float:
        if len(self.less) > len(self.greater):
            return self.less[0] * -1
        return (self.less[0] * -1 + self.greater[0]) / 2
        