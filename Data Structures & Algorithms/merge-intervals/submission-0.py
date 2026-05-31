class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        i = 1
        lastIsOverlapping = False
        while i < len(intervals):
            i1 = intervals[i]
            
            if i1[0] > res[-1][1]: # non overlapping
                res.append(i1)
                i += 1
                # lastIsOverlapping = False
                # print(str(i) + "non-overlapping")
                continue
            
            # overlapping
            # print(str(i) + "overlapping")
            # lastIsOverlapping = True
            res[-1] = [min(i1[0], res[-1][0]), max(i1[1], res[-1][1])]

            # while i < len(intervals) and intervals[i][0] <= intervals[i-1][1]:
            #     newI = [newI[0], max(newI[1], intervals[i][1], intervals[i-1][1])]
            #     i += 1
            # res.append(newI)
            i += 1
        return res