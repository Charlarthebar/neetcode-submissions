class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        qsorted = sorted(queries)
        answers = {}
        heap = []
        i = 0

        for q in qsorted:
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(heap, (e - s + 1, e))
                i += 1
            
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            if heap and q not in answers:
                answers[q] = heap[0][0]
        
        res = []
        for q in queries:
            if q in answers:
                res.append(answers[q])
            else:
                res.append(-1)
        return res