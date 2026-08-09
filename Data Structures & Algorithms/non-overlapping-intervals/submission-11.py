class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end = intervals[0][0]
        res = 0

        for s, e in intervals:
            if s < end:
                res += 1
                end = min(end, e)
            else:
                end = e
        return res