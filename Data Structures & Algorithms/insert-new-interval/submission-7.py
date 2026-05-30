class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        a, b = 0, len(intervals)
        for i in range(len(intervals)):
            start, end = intervals[i]
            if start < newInterval[0] and end < newInterval[0]:
                a = i + 1
            elif start > newInterval[0] and end > newInterval[0]:
                b = min(b, i)
            if end >= newInterval[0] and start <= newInterval[1]:
                new_start = min(new_start, start)
                new_end = max(new_end, end)
                a = i
                j = i
                while j < len(intervals) and intervals[j][1] >= newInterval[0] and intervals[j][0] <= newInterval[1]:
                    new_start = min(new_start, intervals[j][0])
                    new_end = max(new_end, intervals[j][1])
                    j += 1
                b = j
                break
        print(a, b)
        return intervals[:a] + [[new_start, new_end]] + intervals[b:]