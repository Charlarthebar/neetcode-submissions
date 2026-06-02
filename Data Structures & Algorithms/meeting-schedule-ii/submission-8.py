"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = [(i.start, "start") for i in intervals] + [(i.end, "end") for i in intervals]
        times.sort(key=lambda x: (x[0], x[1]))
        print(times)
        res = 0
        count = 0
        for time, typ in times:
            if typ == "start":
                count += 1
                res = max(res, count)
            else:
                count -= 1
        return res