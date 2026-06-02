"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [interval.start for interval in intervals]
        start.sort()
        end = [interval.end for interval in intervals]
        end.sort()
        print(start)
        print(end)

        p1, p2 = 0, 0
        res = 0
        cur_meetings = 0
        while p1 < len(start):
            print(cur_meetings, res)
            print(start[p1], end[p2])
            print()
            if start[p1] < end[p2]:
                cur_meetings += 1
                res = max(res, cur_meetings)
                p1 += 1
            else:
                cur_meetings -= 1
                p2 += 1
            
        return res