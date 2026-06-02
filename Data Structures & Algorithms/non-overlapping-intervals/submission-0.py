class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        prevEnd = intervals[0][1]
        counter = 0

        for start, end in intervals[1:]:
            if start < prevEnd:
                counter += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
        return counter
            