class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.tmap[key]) - 1
        res = ""
        while l <= r:
            m = l + (r - l) // 2
            if self.tmap[key][m][0] <= timestamp:
                l = m + 1
                res = self.tmap[key][m][1]
            else:
                r = m - 1
        return res
