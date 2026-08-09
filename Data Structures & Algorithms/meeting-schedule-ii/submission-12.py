"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts, ends = defaultdict(int), defaultdict(int)
        times = set()

        for interval in intervals:
            start, end = interval.start, interval.end
            starts[start] += 1
            ends[end] += 1
            times.add(start)
            times.add(end)
        
        res = 0
        cur = 0
        for t in sorted(list(times)):
            cur += starts[t]
            cur -= ends[t]
            res = max(res, cur)
        return res