class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] = 1 + self.points.get(tuple(point), 0)

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        for x2, y2 in self.points:
            dx, dy = abs(x2 - x1), abs(y2 - y1)
            if dx == dy and dx != 0 and (x1, y2) in self.points and (x2, y1) in self.points:
                cur = self.points[(x2, y2)] * self.points[(x1, y2)] * self.points[(x2, y1)]
                res += cur
        return res
